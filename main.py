import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.client.default import DefaultBotProperties

from config import TELEGRAM_TOKEN
from handlers import get_routers

# ============================================
# ІНІЦІАЛІЗАЦІЯ БОТА
# ============================================

# Створюємо екземпляр бота з токеном та налаштуваннями за замовчуванням
# parse_mode="HTML" дозволяє використовувати HTML розмітку в повідомленнях (<b>, <i> тощо)
bot = Bot(TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

# Створюємо диспетчер для обробки оновлень від Telegram
dp = Dispatcher()


# ============================================
# НАЛАШТУВАННЯ КОМАНД БОТА
# ============================================

async def set_commands(bot: Bot):
    """
    Встановлює список команд, які відображаються в меню бота
    Ці команди з'являються при натисканні "/" в полі вводу Telegram
    """
    commands = [
        BotCommand(command="start", description="Launch the bot / Refresh the menu"),
        BotCommand(command="rn", description="Random number within a range (e.g.: /rn 1-100)"),
    ]
    await bot.set_my_commands(commands)


# ============================================
# ГОЛОВНА ФУНКЦІЯ ЗАПУСКУ
# ============================================

async def main():
    """
    Головна функція для запуску бота

    Послідовність дій:
    1. Підключає всі роутери (обробники) з папки handlers
    2. Встановлює команди бота в меню
    3. Видаляє webhook (якщо був встановлений) для роботи через polling
    4. Запускає long polling для отримання оновлень від Telegram
    """
    # Підключаємо всі роутери з handlers/__init__.py
    dp.include_routers(*get_routers())

    # Встановлюємо команди в меню бота
    await set_commands(bot)

    # Видаляємо webhook та скидаємо всі накопичені оновлення
    # drop_pending_updates=True - ігнорує всі повідомлення, які прийшли під час простою бота
    await bot.delete_webhook(drop_pending_updates=True)

    print("Bot started")
    # Запускаємо long polling - бот буде постійно перевіряти нові оновлення
    await dp.start_polling(bot)


# ============================================
# ТОЧКА ВХОДУ
# ============================================

if __name__ == "__main__":
    try:
        # Запускаємо асинхронну головну функцію
        asyncio.run(main())
    except KeyboardInterrupt:
        # Обробка зупинки бота через Ctrl+C
        print("Bot stopped")