from aiogram.types import (
ReplyKeyboardMarkup,
KeyboardButton,
InlineKeyboardMarkup,
InlineKeyboardButton
)

# ============================================
# ГОЛОВНЕ МЕНЮ (Reply Keyboard)
# ============================================

# Головна клавіатура з основними функціями бота
# resize_keyboard=True - автоматично підбирає розмір кнопок
# one_time_keyboard=True - клавіатура ховається після натискання
# input_field_placeholder - підказка в полі вводу
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="links"),           # Корисні посилання
            KeyboardButton(text="finding area")     # Калькулятор площ
        ],
        [
            KeyboardButton(text="chat with Ai"),    # Чат з Gemini AI
            KeyboardButton(text="other")            # Додаткові функції
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="виберіть щось",
    selective=True,
)

# ============================================
# INLINE КЛАВІАТУРИ (з посиланнями та callback)
# ============================================
categories_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Useful links", callback_data="links_useful")
        ],
        [
            InlineKeyboardButton(text="Funny links", callback_data="links_funny")
        ],
        [
            InlineKeyboardButton(text="◀️ back", callback_data="main_menu")
        ]
    ]
)

links_funny_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🟥 YouTube - your wishlist", url="https://www.youtube.com/playlist?list=WL"),
        ],
        [
            InlineKeyboardButton(text="🌍 а window to any corner of the world", url="https://www.window-swap.com/Window")
        ],
        [
            InlineKeyboardButton(text="🎮 Addictive mini-games", url="https://neal.fun")
        ],
        [
            InlineKeyboardButton(text="◀️ back", callback_data="main_links")
        ]
    ]
)

links_useful_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🟥 YouTube - your wishlist", url="https://www.youtube.com/playlist?list=WL"),
        ],
        [
            InlineKeyboardButton(text="🍽️ Restorant - the author's website", url="https://restorant-d84f8.firebaseapp.com/")
        ],
        [
            InlineKeyboardButton(text="🌱 Fitlife - the author's other website", url="https://fitlife-a5343.firebaseapp.com/")
        ],
        [
            InlineKeyboardButton(text="📩 Temporary email (10 min)", url="https://10minutemail.com")
        ],
        [
            InlineKeyboardButton(text="️💻 a stylish screenshot of the code", url="https://carbon.now.sh")
        ],
        [
            InlineKeyboardButton(text="📊 Check your internet speed", url="https://fast.com")
        ],
        [
            InlineKeyboardButton(text="◀️ back", callback_data="main_links")
        ]
    ]
)

# Клавіатура для вибору геометричної фігури
# callback_data - дані, які передаються обробнику при натисканні
areas_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="square", callback_data="square_area"),      # Квадрат
            InlineKeyboardButton(text="circle", callback_data="circle_area")       # Коло
        ],
        [
            InlineKeyboardButton(text="triangle", callback_data="triangle_area")   # Трикутник
        ]
    ]
)

# Спеціальні кнопки для додаткових функцій
special_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Button 1", callback_data="special_1"),
            InlineKeyboardButton(text="Button 2", callback_data="special_2"),
            InlineKeyboardButton(text="Button 3", callback_data="special_3")
        ]
    ]
)

# ============================================
# ДОПОМІЖНІ КЛАВІАТУРИ
# ============================================

# Клавіатура для скасування дії (використовується в режимі AI чату)
calcel_kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="cancel")]  # Кнопка для виходу з поточного режиму
        ],
    resize_keyboard=True,
    )