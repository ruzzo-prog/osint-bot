# OSINT Telegram Bot — Инструкция по проекту

## 📌 Описание
Проект представляет собой Telegram-бота, который осуществляет поиск информации по ИНН организаций через открытые источники (например, API dadata.ru). Такой бот используется в OSINT-целях для получения официальной информации по юридическим лицам.

Проект легко расширяем и может быть дополнен следующими функциями:
- Поиск по номеру телефона (через базы и API)
- Проверка VIN и госномеров авто
- Поиск по ФИО, адресам, email
- Распознавание по Telegram username / user ID

---

## 📁 Структура проекта
```
D:	elbot\
├── bot.py                # Главный файл Telegram-бота
├── config.py             # Конфигурация и загрузка переменных окружения
├── bot.py                # Главный файл Telegram-бота
├── .env                  # Хранит секреты: TELEGRAM_TOKEN и DADATA_API_KEY
├── requirements.txt      # Список зависимостей
├── README.md             # Документация и инструкция
├── venv\                 # Виртуальное окружение Python
└── services\             # Логика и модули (поиск по ИНН, телефону и др.)
```

---

## ⚙️ Настройка окружения

### 1. Создание проекта
Создайте папку:
```bash
mkdir D:\telbot
cd D:\telbot
```

### 2. Виртуальное окружение
Создайте и активируйте виртуальную среду Python:
```bash
cd D:\telbot
py -3.11 -m venv telbot311
telbot311\Scripts\activate

 # для Windows
```

### 3. Установка зависимостей
Создайте файл `requirements.txt` со следующим содержанием:
```txt
aiogram
requests
python-dotenv
```
Затем установите:
```bash
pip install -r requirements.txt
```

### 4. Файл .env
Создайте `.env` с переменными:
```env
TELEGRAM_TOKEN=токен_бота_от_BotFather
DA_DATA_API_KEY=ключ_от_dadata.ru
```

---

## 🔧 Расширения и модули
В папке `services/` могут размещаться вспомогательные модули:
- `inn_lookup.py` — логика поиска по ИНН
- `phone_lookup.py` — логика поиска по номеру телефона (будущее)
- `logger.py` — логирование
- `vin_lookup.py` — проверка авто

Также можно добавить:
- SQLite базу для хранения истории
- Webhook-режим (для деплоя на сервер)
- Личный кабинет пользователя (через Telegram ID)

---

## 🛡 Безопасность
- Всегда сохраняйте `.env` в `.gitignore`
- Не выкладывайте токены в публичные репозитории
- Используйте виртуальное окружение (`venv`) для изоляции

---

## ✅ Статус
На текущем этапе реализован функционал по приёму ИНН и выдаче информации о компании. Готов к расширению.

Если необходимо — подключим сторонние базы, API, или сделаем полноценную OSINT-панель на Flask/React.


Luis Loren, [18.05.2025 18:50]
/newbot

BotFather, [18.05.2025 18:50]
Alright, a new bot. How are we going to call it? Please choose a name for your bot.

Luis Loren, [18.05.2025 18:50]
MyOsintBot

BotFather, [18.05.2025 18:50]
Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.

Luis Loren, [18.05.2025 18:51]
osinthelper_bot

BotFather, [18.05.2025 18:51]
Sorry, this username is already taken. Please try something different.

Luis Loren, [18.05.2025 18:52]
osint_assist_bot

BotFather, [18.05.2025 18:52]
Done! Congratulations on your new bot. You will find it at t.me/osint_assist_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
7823223256:AAEwCIQL30vZYV3mrRIgLKhTH6yNQM8Fxn4
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
