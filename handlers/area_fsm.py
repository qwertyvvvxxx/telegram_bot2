from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import math
from aiogram.fsm.state import State, StatesGroup

router = Router()

class AreaStates(StatesGroup):
    waiting_for_square_side = State()
    waiting_for_circle_radius = State()
    waiting_for_triangle_base = State()
    waiting_for_triangle_height = State()

@router.callback_query(F.data == "square_area")
async def square_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("📐 Calculating the Area of a Square.\nEnter the side length:")

    await state.set_state(AreaStates.waiting_for_square_side)

@router.callback_query(F.data == "circle_area")
async def square_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("📐 Calculating the Area of a Circle.\nEnter the radius:")

    await state.set_state(AreaStates.waiting_for_circle_radius)

@router.callback_query(F.data == "triangle_area")
async def triangle_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("📐 Calculating the Area of a Triangle.\nEnter the length of the base of the triangle:")
    await state.set_state(AreaStates.waiting_for_triangle_base)

# ---- ОБЧИСЛЕННЯ ПЛОЩ ----

@router.message(AreaStates.waiting_for_square_side)
async def process_square(message: Message, state: FSMContext):
    try:
        side = float(message.text)
        if side <= 0:
            raise ValueError
        else:
            area = side ** 2
            await message.answer(f"✅ The area of a square with a side length of {side} is: <b>{area:.2f}</b>")
        await state.clear()
    except ValueError:
        await message.answer("❌ Enter a valid number (greater than 0, and use a period instead of a comma):")

@router.message(AreaStates.waiting_for_circle_radius)
async def process_circle(message: Message, state: FSMContext):
    try:
        radius = float(message.text)
        if radius <= 0:
            raise ValueError

        area = math.pi * (radius ** 2)
        await message.answer(f"✅ The area of a circle with radius {radius} is: <b>{area:.2f}</b>")
        await state.clear()
    except ValueError:
        await message.answer("❌ Enter a valid number (greater than 0, and use a period instead of a comma):")

@router.message(AreaStates.waiting_for_triangle_base)
async def process_triangle_base(message: Message, state: FSMContext):
    try:
        base = float(message.text)
        if base <= 0:
            raise ValueError
        await state.update_data(base=base)
        await message.answer("Great! Now enter the height of the triangle:")

        await state.set_state(AreaStates.waiting_for_triangle_height)
    except ValueError:
        await message.answer("❌ Enter a valid number (greater than 0, and use a period instead of a comma):")

@router.message(AreaStates.waiting_for_triangle_height)
async def process_triangle_height(message: Message, state: FSMContext):
    try:
        height = float(message.text)
        if height <= 0:
            raise ValueError

        user_data = await state.get_data()
        base = user_data.get("base")

        area = 0.5 * base * height
        await message.answer(f"✅ The area of a triangle (base {base}, height {height}) is: <b>{area:.2f}</b>")
        await state.clear()
    except ValueError:
        await message.answer("❌ Enter a valid number (greater than 0, and use a period instead of a comma):")