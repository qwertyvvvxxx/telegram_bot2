from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
import keyboards
from handlers.gemini import GeminiStates

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

@router.message(F.text.lower() == "chat with ai")
async def start_gemini(message: Message, state: FSMContext):
    await state.set_state(GeminiStates.wait_for_prompt)
    await message.answer("Gemini started, what we will do?", reply_markup=keyboards.calcel_kb)


# ІНЛАЙН-КНОПОКИ

@router.callback_query(F.data.startswith("special_"))
async def process_special_buttons(callback: CallbackQuery):
    button_number = callback.data.split("_")[1]
    await callback.answer()
    await callback.message.answer(f"You pressed the special button №{button_number}")

@router.message()
async def echo_fallback(message: Message):
    await message.answer("I don`t understand this command")