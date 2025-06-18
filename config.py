# config.py — конфигурация
# Путь: D:\telbot\config.py

import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DA_DATA_API_KEY = os.getenv("DA_DATA_API_KEY")
