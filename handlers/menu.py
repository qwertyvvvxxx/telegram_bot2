from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
import keyboards
from handlers.gemini import GeminiStates

# Створення роутера для обробки меню
router = Router()

# ============================================
# ОБРОБНИКИ КНОПОК ГОЛОВНОГО МЕНЮ
# ============================================

@router.message(F.text.lower() == "links")
async def show_links(message: Message):
    """
    Обробляє натискання кнопки "links"
    Показує inline клавіатуру з корисними посиланнями
    """
    await message.answer("Your links:", reply_markup=keyboards.links_kb)

@router.message(F.text.lower() == "finding area")
async def show_areas(message: Message):
    """
    Обробляє натискання кнопки "finding area"
    Показує inline клавіатуру з вибором геометричних фігур для обчислення площі
    """
    await message.answer("Select a shape:", reply_markup=keyboards.areas_kb)

@router.message(F.text.lower() == "other")
async def show_other(message: Message):
    """
    Обробляє натискання кнопки "other"
    Показує додаткові спеціальні кнопки
    """
    await message.answer("Other functions:", reply_markup=keyboards.special_kb)

@router.message(F.text.lower() == "chat with ai")
async def start_gemini(message: Message, state: FSMContext):
    """
    Обробляє натискання кнопки "chat with Ai"
    - Переводить користувача в режим спілкування з Gemini AI
    - Встановлює FSM стан очікування prompt'а
    - Показує кнопку "cancel" для виходу з режиму
    """
    await state.set_state(GeminiStates.wait_for_prompt)
    await message.answer("Gemini started, what we will do?", reply_markup=keyboards.calcel_kb)


# ============================================
# ОБРОБНИКИ INLINE КНОПОК
# ============================================

@router.callback_query(F.data.startswith("special_"))
async def process_special_buttons(callback: CallbackQuery):
    """
    Обробляє натискання спеціальних inline кнопок (special_1, special_2, special_3)
    - Витягує номер кнопки з callback_data
    - Відповідає користувачу, яку кнопку він натиснув
    """
    button_number = callback.data.split("_")[1]  # Витягуємо номер з "special_1" → "1"
    await callback.answer()  # Підтверджуємо отримання callback (прибирає "годинник" на кнопці)
    await callback.message.answer(f"You pressed the special button №{button_number}")

# ============================================
# FALLBACK ОБРОБНИК
# ============================================

@router.message()
async def echo_fallback(message: Message):
    """
    Обробляє всі повідомлення, які не були оброблені іншими handlers
    Цей обробник спрацьовує останнім, якщо жоден інший не підійшов
    """
    await message.answer("I don`t understand this command")