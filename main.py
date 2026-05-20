import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.client.default import DefaultBotProperties

from config import TELEGRAM_TOKEN
from handlers import get_routers






from handlers.commands import router as commands_router
from handlers.menu import router as menu_router





bot = Bot(TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Launch the bot / Refresh the menu"),
        BotCommand(command="rn", description="Random number within a range (e.g.: /rn 1-100)"),
    ]
    await bot.set_my_commands(commands)


async def main():
    dp.include_router(commands_router)

    dp.include_router(menu_router)

    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)

    print("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")