from aiogram import Router
from . import commands, menu, area_fsm, gemini


def get_routers() -> list[Router]:
    """
    Повертає список всіх роутерів у правильному порядку пріоритету

    Порядок важливий! Роутери обробляються послідовно:
    1. commands - базові команди (/start, /rn)
    2. area_fsm - калькулятор площ (використовує FSM стани)
    3. gemini - обробка AI запитів (використовує FSM стани)
    4. menu - обробка меню та fallback для невідомих команд (повинен бути останнім!)
    """
    return [
        commands.router,
        area_fsm.router,
        gemini.router,
        menu.router  # Завжди останній, тому що містить fallback обробник
    ]