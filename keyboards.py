from aiogram.types import (
ReplyKeyboardMarkup,
KeyboardButton,
InlineKeyboardMarkup,
InlineKeyboardButton
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="links"),
            KeyboardButton(text="finding area")
        ],
        [
            KeyboardButton(text="chat with Ai"),
            KeyboardButton(text="other")
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
        ],
        [
            InlineKeyboardButton(text="Restorant", url="https://restorant-d84f8.firebaseapp.com/")
        ],
        [
            InlineKeyboardButton(text="Fitlife", url="https://fitlife-a5343.firebaseapp.com/")
        ]
    ]
)

areas_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="square", callback_data="square_area"),
            InlineKeyboardButton(text="circle", callback_data="circle_area")
        ],
        [
            InlineKeyboardButton(text="triangle", callback_data="triangle_area")
        ]
    ]
)

special_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Button 1", callback_data="special_1"),
            InlineKeyboardButton(text="Button 2", callback_data="special_2"),
            InlineKeyboardButton(text="Button 3", callback_data="special_3")
        ]
    ]
)

calcel_kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="cancel")]
        ],
    resize_keyboard=True,
    )