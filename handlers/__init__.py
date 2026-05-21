from aiogram import Router
from . import commands, menu, area_fsm

def get_routers() -> list[Router]:
    return [
        commands.router,
        area_fsm.router,
        menu.router
    ]