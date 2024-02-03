# DLS Telegram bot для Real-ESRGAN от Сбера
Данный телеграм бот увеличивает изображение в 4 раза.
Я взял готовую претрейн [модель](https://github.com/ai-forever/Real-ESRGAN/tree/main) от ai-forever (зеленый известный *стартап*), которую они сделали на основе Real-ESRGAN. 

Обвязка модели и сам Pytorch код использован также из репозитория ai-forever.

### Usage

---
1. Создать .env файл, добавить в него `TG_BOT_TOKEN='токен_вашего_телеграм_бота'`
2. Запустите app.py в корне репозитория.


### Примеры

---

Исходное изображение:

![](inputs/lr_image.png)

Результат:

![](results/sr_image.png)

---

Исходное изображение:

![](inputs/lr_face.png)

Результат:

![](results/sr_face.png)

---
