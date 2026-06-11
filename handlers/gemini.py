from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from config import ai_client
import keyboards

# Створення роутера для обробки AI запитів
router = Router()

# ============================================
# FSM СТАНИ ДЛЯ GEMINI AI
# ============================================

class GeminiStates(StatesGroup):
    """
    Стани для роботи з Gemini AI
    wait_for_prompt - стан очікування повідомлення від користувача для відправки в AI
    """
    wait_for_prompt = State()

# ============================================
# ОБРОБНИКИ РЕЖИМУ GEMINI AI
# ============================================

@router.message(GeminiStates.wait_for_prompt, F.text == "cancel")
async def cancel_gemini(message: Message, state: FSMContext):
    """
    Обробляє натискання кнопки "cancel" в режимі AI
    - Виходить з режиму AI (очищає стан FSM)
    - Повертає користувача до головного меню
    """
    await state.clear()
    await message.answer("You've left AI mode", reply_markup=keyboards.main_kb)


@router.message(GeminiStates.wait_for_prompt)
async def handle_gemini_request(message: Message):
    """
    Обробляє запити користувача до Gemini AI

    Логіка роботи:
    1. Отримує текст від користувача
    2. Відображає індикатор "typing..." в чаті
    3. Відправляє запит до Google Gemini API (модель gemini-2.5-flash)
    4. Розбиває довгі відповіді на частини по 4000 символів (обмеження Telegram)
    5. Логує запити та відповіді в консоль
    """
    user_fullname = message.from_user.full_name
    user_prompt = message.text

    # Показуємо індикатор "печатає..." в чаті
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")

    try:
        # Відправляємо запит до Gemini API
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',  # Використовуємо швидку модель Flash
            contents=user_prompt,
        )
        full_text = response.text

        # Telegram має обмеження на довжину повідомлень - 4096 символів
        # Тому розбиваємо довгі відповіді на частини
        LIMIT = 4000

        if len(full_text) <= LIMIT:
            # Якщо текст короткий - відправляємо одним повідомленням
            await message.answer(full_text, parse_mode="HTML")
        else:
            # Якщо текст довгий - розбиваємо на частини по 4000 символів
            for i in range(0, len(full_text), LIMIT):
                chunk = full_text[i:i + LIMIT]
                await message.answer(chunk)

        # Логування повної відповіді для відстеження
        print(f"\n[Gemini Request] User: {user_fullname} | Prompt: {user_prompt} | Full text: {full_text}")

    except Exception as e:
        # Обробка помилок (наприклад, перевищення квоти API, проблеми з мережею)
        await message.answer(text="Ops error please try again later", reply_markup=keyboards.main_kb)
        print(f"Gemini Error: {e}")
