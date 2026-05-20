from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import keyboards

router = Router()

@router.message(F.text.lower() == "links")
async def show_links(message: Message):
    await message.answer("Your links:", reply_markup=keyboards.links_kb)

@router.message(F.text.lower() == "finding area")
async def show_areas(message: Message):
    await message.answer("Select a shape:", reply_markup=keyboards.areas_kb)

@router.message(F.text.lower() == "other")
async def show_other(message: Message):
    await message.answer("Other functions:", reply_markup=keyboards.special_kb)

@router.message(F.text.lower() == "calculator")
async def show_calculator(message: Message):
    await message.answer("This feature has not been implemented yet ")


# ІНЛАЙН-КНОПОКИ

@router.callback_query(F.data == "square_area")
async def process_square(callback: CallbackQuery):
    await callback.answer("You have selected a square")
    await callback.message.answer("here will be a script to find areas")

@router.callback_query(F.data == "circle_area")
async def process_square(callback: CallbackQuery):
    await callback.answer("You have selected a circle")
    await callback.message.answer("here will be a script to find areas")

@router.callback_query(F.data == "triangle_area")
async def process_square(callback: CallbackQuery):
    await callback.answer("You have selected a triangle")
    await callback.message.answer("here will be a script to find areas")

@router.callback_query(F.data.startswith("special_"))
async def process_special_buttons(callback: CallbackQuery):
    button_number = callback.data.split("_")[1]
    await callback.answer()
    await callback.message.answer(f"You pressed the special button №{button_number}")

@router.message()
async def echo_fallback(message: Message):
    await message.answer("I don`t understand this command")