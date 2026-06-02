from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from config import ai_client
import keyboards

router = Router()

class GeminiStates(StatesGroup):
    wait_for_prompt = State()

@router.message(GeminiStates.wait_for_prompt, F.text == "cancel")
async def cancel_gemini(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("You've left AI mode", reply_markup=keyboards.main_kb)


@router.message(GeminiStates.wait_for_prompt)
async def handle_gemini_request(message: Message):
    user_fullname = message.from_user.full_name
    user_prompt = message.text

    print(f"\n[Gemini Request] User: {user_fullname} | Prompt: {user_prompt}")

    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    try:
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
        )
        full_text = response.text

        LIMIT = 4000

        if len(full_text) <= LIMIT:
            await message.answer(full_text, parse_mode="HTML")
        else:
            for i in range(0, len(full_text), LIMIT):
                chunk = full_text[i:i + LIMIT]
                await message.answer(chunk)
        print(f"\n[Gemini Request] User: {user_fullname} | Prompt: {user_prompt} | Full text: {full_text}")
    except Exception as e:
        await message.answer(text="Ops error please try again later", reply_markup=keyboards.main_kb)
        print(f"Gemini Error: {e}")
