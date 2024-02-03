import logging

# Настраиаем логгер
def logger():
	logger = logging.getLogger('my_logger')
	logger.setLevel(logging.DEBUG)
	handler = logging.FileHandler('bot_logs.log')
	handler.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	return logger