from PIL import Image
import uuid
import os

# Генерация картинки
def get_upscale(img_path: str, model) -> str:
	image = Image.open(img_path).convert('RGB')
	sr_image = model.predict(image)
	img_upscaled_path = './upscaled/' + str(uuid.uuid4()) + '.png'
	sr_image.save(img_upscaled_path)
	return img_upscaled_path


# Обработчик вопроса
def process_requests(message, file_type: str, bot, model, logger) -> int:
	user_id = message.from_user.id
	username = message.from_user.username
	logger.info('Запрошена картинка user_id: %s, username: %s', user_id, username)
	bot.send_chat_action(message.chat.id, 'typing')

	try:
		# Запрос может придти как в виде изображения, так и в виде файла.
		if (file_type == 'photo'):
			# Загружаем и сохраняем файл
			file_info = bot.get_file(message.photo[-1].file_id)
			downloaded_file = bot.download_file(file_info.file_path)
			extension = file_info.file_path.split('.')[-1]
			random_filename = str(uuid.uuid4())
			img_path = './incoming/'+random_filename+'.'+extension

			with open(img_path, 'wb') as new_file:
				new_file.write(downloaded_file)

		if (file_type == 'document'):
			file_info = bot.get_file(message.document.file_id)
			file_extension = file_info.file_path.split('.')[-1]

			if file_extension in ['jpg', 'jpeg', 'png']:
				downloaded_file = bot.download_file(file_info.file_path)
				random_filename = str(uuid.uuid4())
				img_path = './incoming/' + random_filename + '.' + file_extension

				with open(img_path, 'wb') as new_file:
					new_file.write(downloaded_file)
			else:
				bot.reply_to(message, 'Надо фотографию ☺️')
				return 0


		# Увеличиваем, сохраняем, отправляем как файл
		img_upscaled_path = get_upscale(img_path, model)

		with open(img_upscaled_path, 'rb') as img:
			bot.send_document(message.chat.id, img)


		# Удаляем картинки чтобы не копить (мало ли что там пришлют?)
		os.remove(img_path)
		os.remove(img_upscaled_path)

		# Возвращаем возможность обработки.
		return 1

	except Exception as n:
		logger.error(n)
		bot.reply_to(message, 'Произошла ошибка при обработке запроса')
		# Возвращаем возможность обработки.
		return 1
