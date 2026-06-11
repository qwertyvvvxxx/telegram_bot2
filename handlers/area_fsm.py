from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
import math
from aiogram.fsm.state import State, StatesGroup

# Створення роутера для обробки калькулятора площ
router = Router()

# ============================================
# FSM СТАНИ ДЛЯ КАЛЬКУЛЯТОРА ПЛОЩ
# ============================================

class AreaStates(StatesGroup):
    """
    Стани для обчислення площі різних геометричних фігур
    Кожен стан відповідає очікуванню певного параметра від користувача
    """
    waiting_for_square_side = State()       # Очікування довжини сторони квадрата
    waiting_for_circle_radius = State()     # Очікування радіуса кола
    waiting_for_triangle_base = State()     # Очікування довжини основи трикутника
    waiting_for_triangle_height = State()   # Очікування висоти трикутника

# ============================================
# ОБРОБНИКИ INLINE КНОПОК (початок обчислення)
# ============================================

@router.callback_query(F.data == "square_area")
async def square_start(callback: CallbackQuery, state: FSMContext):
    """
    Початок обчислення площі квадрата
    Встановлює стан очікування введення довжини сторони
    """
    await callback.answer()  # Підтверджуємо отримання callback
    photo = FSInputFile("resources/square-a-side.png")
    await callback.message.answer_photo(photo)

    await callback.message.answer("📐 Calculating the Area of a Square.\nEnter the side length:")
    await state.set_state(AreaStates.waiting_for_square_side)

@router.callback_query(F.data == "circle_area")
async def circle_area_start(callback: CallbackQuery, state: FSMContext):
    """
    Початок обчислення площі кола
    Встановлює стан очікування введення радіуса
    """
    await callback.answer()
    photo = FSInputFile("resources/circle.png")
    await callback.message.answer_photo(photo)

    await callback.message.answer("📐 Calculating the Area of a Circle.\nEnter the radius:")
    await state.set_state(AreaStates.waiting_for_circle_radius)

@router.callback_query(F.data == "triangle_area")
async def triangle_start(callback: CallbackQuery, state: FSMContext):
    """
    Початок обчислення площі трикутника
    Встановлює стан очікування введення довжини основи
    Для трикутника потрібно 2 параметри: основа і висота (двокрокове введення)
    """
    await callback.answer()
    photo = FSInputFile("resources/triangle_base.png")
    await callback.message.answer_photo(photo)

    await callback.message.answer("📐 Calculating the Area of a Triangle.\nEnter the length of the base of the triangle:")
    await state.set_state(AreaStates.waiting_for_triangle_base)

# ============================================
# ОБЧИСЛЕННЯ ПЛОЩ
# ============================================

@router.message(AreaStates.waiting_for_square_side)
async def process_square(message: Message, state: FSMContext):
    """
    Обчислює площу квадрата за формулою: S = a²

    Валідація:
    - Перевіряє, чи введено число
    - Перевіряє, чи число більше 0
    """
    try:
        side = float(message.text)
        if side <= 0:
            raise ValueError
        else:
            area = side ** 2  # Формула площі квадрата: S = a²
            await message.answer(f"✅ The area of a square with a side length of {side} is: <b>{area:.2f}</b>")
        await state.clear()  # Очищаємо стан після завершення обчислення
    except ValueError:
        # Якщо введено неправильне значення, просимо ввести ще раз
        await message.answer("❌ Enter a valid number (greater than 0, and use a period instead of a comma):")

@router.message(AreaStates.waiting_for_circle_radius)
async def process_circle(message: Message, state: FSMContext):
    """
    Обчислює площу кола за формулою: S = π * r²

    Валідація:
    - Перевіряє, чи введено число
    - Перевіряє, чи число більше 0
    """
    try:
        radius = float(message.text)
        if radius <= 0:
            raise ValueError

        area = math.pi * (radius ** 2)  # Формула площі кола: S = π * r²
        await message.answer(f"✅ The area of a circle with radius {radius} is: <b>{area:.2f}</b>")
        await state.clear()
    except ValueError:
        await message.answer("❌ Enter a valid number (greater than 0, and use a period instead of a comma):")

@router.message(AreaStates.waiting_for_triangle_base)
async def process_triangle_base(message: Message, state: FSMContext):
    """
    Перший крок обчислення площі трикутника - отримання довжини основи
    Зберігає значення в FSM context і переходить до наступного стану (очікування висоти)
    """
    try:
        base = float(message.text)
        if base <= 0:
            raise ValueError

        # Зберігаємо довжину основи в FSM context для наступного кроку
        await state.update_data(base=base)

        photo = FSInputFile("resources/triangle_height.png")
        await message.answer_photo(photo)

        await message.answer("Great! Now enter the height of the triangle:")

        # Переходимо до наступного стану - очікування висоти
        await state.set_state(AreaStates.waiting_for_triangle_height)
    except ValueError:
        await message.answer("❌ Enter a valid number (greater than 0, and use a period instead of a comma):")

@router.message(AreaStates.waiting_for_triangle_height)
async def process_triangle_height(message: Message, state: FSMContext):
    """
    Другий крок обчислення площі трикутника - отримання висоти
    Обчислює площу за формулою: S = (a * h) / 2

    Використовує збережене значення основи з FSM context
    """
    try:
        height = float(message.text)
        if height <= 0:
            raise ValueError

        # Отримуємо збережене значення основи з FSM context
        user_data = await state.get_data()
        base = user_data.get("base")

        # Формула площі трикутника: S = (a * h) / 2
        area = 0.5 * base * height
        await message.answer(f"✅ The area of a triangle (base {base}, height {height}) is: <b>{area:.2f}</b>")
        await state.clear()  # Очищаємо всі збережені дані та стан
    except ValueError:
        await message.answer("❌ Enter a valid number (greater than 0, and use a period instead of a comma):")