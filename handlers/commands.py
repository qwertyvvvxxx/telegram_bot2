import random
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
import keyboards

# Створення роутера для обробки команд
router = Router()


# ============================================
# КОМАНДА /start
# ============================================

@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    """
    Обробляє команду /start
    - Очищає всі активні стани FSM
    - Вітає користувача за ім'ям
    - Відображає головне меню
    """
    await state.clear()  # Скидаємо всі попередні стани (якщо користувач був у режимі AI чи калькулятора)
    await message.answer(f"Hello, <b>{message.from_user.full_name}</b>", reply_markup=keyboards.main_kb)


# ============================================
# КОМАНДА /rn (Random Number)
# ============================================

@router.message(Command("random_number", "rn"))
async def random_number(message: Message, command: CommandObject):
    """
    Генерує випадкове число в заданому діапазоні
    Формат: /rn x-y (наприклад: /rn 1-100)

    Параметри:
    - command.args: рядок виду "x-y", де x та y - межі діапазону

    Приклади використання:
    - /rn 1-10 → випадкове число від 1 до 10
    - /rn 50-100 → випадкове число від 50 до 100
    """
    try:
        # Перевіряємо, чи передано аргументи команди
        if not command.args:
            raise ValueError

        # Розбиваємо рядок "x-y" на два числа
        a, b = [int(n) for n in command.args.split("-")]

        # Генеруємо випадкове число в діапазоні [a, b]
        rnum = random.randint(a, b)

        await message.reply(f"<b>{rnum}</b>")
    except (ValueError, IndexError):
        # Якщо формат неправильний, показуємо помилку
        await message.reply("<b>ops error! \nPlease write in the correct format (x-y)</b>")