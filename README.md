# DLS Telegram bot для Real-ESRGAN от Сбера
Данный телеграм бот увеличивает изображение в 4 раза.
Я взял готовую претрейн [модель](https://github.com/ai-forever/Real-ESRGAN/tree/main) от ai-forever (зеленый известный *стартап*), которую они сделали на основе Real-ESRGAN. 

Их модель в сравнении с оригиналом Real-ESRGAN дотренирована на лица.

Обвязка модели и сам Pytorch код использован также из репозитория ai-forever.

### Запуск

---
1. Создать .env файл, добавить в него `TG_BOT_TOKEN='токен_вашего_телеграм_бота'`
2. Запустите app.py в корне репозитория.


### Примеры

---

Исходное изображение:

![](incoming/dls.png)

Результат:

![](upscaled/dls_upscaled.png)

---

Исходное изображение:

![](incoming/woman.png)

Результат:

![](upscaled/woman_upscaled.png)

---
