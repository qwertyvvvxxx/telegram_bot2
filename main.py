import asyncio
import os
import random

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, BotCommand
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandObject

from dotenv import load_dotenv

import keyboards


load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f"Hello, <b>{message.from_user.full_name}</b>", reply_markup=keyboards.main_kb)

@dp.message(Command("random_number", "rn")) # rn 1-100
async def random_number(message: Message, command: CommandObject):
    try:
        a, b = [int(n) for n in command.args.split("-")] # [1, 100]

        rnum = random.randint(a, b)

        await message.reply(f"<b>{rnum}</b>")

    except:

        await message.reply(
            f"<b>ops eror! \n"
            f"Please write in the correct format (x-y)</b>"
        )

@dp.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "посилання":
        await message.answer("Ось ваші посилання:", reply_markup=keyboards.links_kb)
    elif msg == "площі фігур":
        await message.answer("Виберіть фігуру для знаходження площі", reply_markup=keyboards.areas_kb)
    else:
        await message.answer("I don`t understand this command")

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустити бота / Оновити меню"),
        BotCommand(
            command="rn",
            description="Випадкове число в діапазоні (наприклад: /rn 1-100)",
        ),
    ]
    # Реєструємо команди в Telegram
    await bot.set_my_commands(commands)

async def main():
    await set_commands(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    print("bot started successfully")
else:
    print("Eror")