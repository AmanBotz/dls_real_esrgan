import os
import telebot
import json
import codecs
import requests 
import sys
from telebot import types
from collections import deque
from dotenv import load_dotenv
from RealESRGAN import RealESRGAN
import torch

from utils import process_requests
from log_util import logger

# Для выводов в консоль без ошибок UTF
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Загружаем токен бота
load_dotenv()
TOKEN = os.getenv("TG_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Загружаем модель в память
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = RealESRGAN(device, scale=4)
model.load_weights('weights/RealESRGAN_x4.pth', download=True)

# Сборщик логов
logger = logger()

# Очередь сообщений, которая позволит боту отвечать даже если идет обработка
# Я возможно ее криво реализовал, через глобальную переменную тут, 
# а нужно было возвращать ее стейт и обновлять, но тут асинхронно все будет, не до конца продумал все ситуации,
# поэтому оставил так — так оно работает =) Наверное следует использовать asyncio
request_queue = deque()

# Это для очереди сообщений, должно быть 1 изначально
is_continue = 1




@bot.message_handler(commands=['start'])
def send_start(message):
	bot.send_message(message.chat.id, "Привет, это бот Real-ESRGAN, он позволяет увеличить изображение в 4 раза. Отправьте мне картинку 🏞️")

# Принимаем все текстовые сообщения в тг бота
@bot.message_handler(content_types=['text'])
def handle_request(message):
	bot.reply_to(message, 'Отправьте фото для увеличения')

# Принимаем все фото сообщения и увеличиваем
@bot.message_handler(content_types=['photo'])
def handle_request(message):
	global is_continue
	global request_queue

	request_queue.append(message)

	file_type = 'photo'
	bot.reply_to(message, 'Обрабатываем...')
	try:
		# Пока в очереди есть сообщения и можно продолжать -- обрабатываем. 
		# Если модель уже отвечает кому-то, но в очереди есть сообщения -- ждем is_continue = 1, 
		# и потом обрабатываем следующее в очереди (а она у нас global)

		while (len(request_queue) > 0 and is_continue == 1):
			# Берем следующее сообщение из очереди.
			message_pop = request_queue.popleft()
			is_continue = 0
			res = process_requests(message_pop, file_type, bot, model, logger)
			is_continue = 1
			
	except Exception as n:
		logger.error(n)
		bot.reply_to(message, 'Произошла ошибка при обработке запроса')

		return 1

@bot.message_handler(content_types=['document'])
def handle_document(message):
	global is_continue
	global request_queue

	request_queue.append(message)

	file_type = 'document'
	bot.reply_to(message, 'Обрабатываем...')
	try:
		while (len(request_queue) > 0 and is_continue == 1):
			# Берем следующее сообщение из очереди.
			message_pop = request_queue.popleft()
			is_continue = 0
			res = process_requests(message_pop, file_type, bot, model, logger)
			is_continue = 1

	except Exception as n:
		logger.error(n)
		bot.reply_to(message, 'Произошла ошибка при обработке запроса')
		# Возвращаем возможность обработки.
		return 1



bot.infinity_polling(timeout=10, long_polling_timeout = 5)