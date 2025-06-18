# bot.py — Telegram OSINT бот
# Путь: D:\telbot\bot.py

from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_TOKEN
from services.inn_lookup import lookup_inn

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


# Команда /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Отправь мне ИНН, и я найду информацию о компании.")


# Обработка текстовых сообщений
@dp.message_handler()
async def handle_message(message: types.Message):
    text = message.text.strip()

    # 🔍 Отладка: логируем, что пришло
    print(
        f"[DEBUG] Получено сообщение: '{text}' (len={len(text)}) isdigit={text.isdigit()}"
    )

    # Проверка на валидный ИНН
    if text.isdigit() and len(text) in [10, 12]:
        result = lookup_inn(text)
        await message.reply(result)
    else:
        await message.reply("❗ Пожалуйста, введи корректный ИНН (10 или 12 цифр).")


# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
