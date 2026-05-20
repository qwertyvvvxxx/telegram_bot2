from aiogram import Router
from . import commands, menu

def get_routers() -> list[Router]:
    return [
        commands.router,
        menu.router
    ]