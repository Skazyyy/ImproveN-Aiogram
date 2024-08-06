from aiogram.types import message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
import app.keyboards as kb 

router = Router()

@router.message(CommandStart())
async def cmd_start(message: message):
    await message.answer("Privet", reply_markup=kb.main)
    await message.reply("Kak dela")


@router.message(Command("help"))
async def cmd_help(message: message):
    await message.answer("Tebe Tolko bog pomoshet")


@router.message(F.text == "Katalog")
async def catalog(message: message):
    await message.answer("Выбери категорию товара", reply_markup=kb.catalog)