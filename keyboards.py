from aiogram.types import (
ReplyKeyboardMarkup,
KeyboardButton,
InlineKeyboardMarkup,
InlineKeyboardButton
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Посилання"),
            KeyboardButton(text="Площі фігур")
        ],
        [
            KeyboardButton(text="калькулятор"),
            KeyboardButton(text="спец. кнопки")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="виберіть щось",
    selective=True,
)

links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/playlist?list=WL"),
        ]
    ]
)

areas_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Квадрат", callback_data="square_area"),
            InlineKeyboardButton(text="Коло", callback_data="circle_area")
        ],
        [
            InlineKeyboardButton(text="Трикутник", callback_data="triangle_area")
        ]
    ]
)