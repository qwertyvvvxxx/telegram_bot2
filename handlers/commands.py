import random
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
import keyboards

router = Router()


@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"Hello, <b>{message.from_user.full_name}</b>", reply_markup=keyboards.main_kb)


@router.message(Command("random_number", "rn"))
async def random_number(message: Message, command: CommandObject):
    try:
        if not command.args:
            raise ValueError

        a, b = [int(n) for n in command.args.split("-")]
        rnum = random.randint(a, b)
        await message.reply(f"<b>{rnum}</b>")
    except (ValueError, IndexError):
        await message.reply("<b>ops error! \nPlease write in the correct format (x-y)</b>")