import os
from dotenv import load_dotenv
from google import genai

# Завантаження змінних середовища з .env файлу
load_dotenv()

# Токен для Telegram бота (отримується від @BotFather)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# API ключ для Google Gemini AI (отримується з Google AI Studio)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Ініціалізація клієнта для роботи з Gemini API
ai_client = genai.Client(api_key=GEMINI_API_KEY)