from aiogram.types import message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
import app.keyboards as kb 
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


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


@router.callback_query(F.data == "Футболка")
async def Футболка(callback: callable):
    await callback.answer("Вы выбрали категорию", show_alert=True)
    await callback.message.answer("Вы выбрали категория футболок")


@router.message(Command("register"))
async def register(message: message, state: FSMContext): 
    await state.set_state(Register.name)
    await message.answer("Введите своё имя")


@router.message(Register.name)
async def register(message: message, state: FSMContext): 
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer("Введите свой возвраст")


@router.message(Register.age)
async def register(message: message, state: FSMContext): 
    await state.update_data(name=message.text)
    await state.set_state(Register.number)
    await message.answer("Введите свой номер телефона", repl_murkup=kb.get_number)


@router.message(Register.number, F.contact)
async def register_number(message: message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f"Ваше имя: {data["name"]}\nВаш возвраст: {data["age"]}\nНомер: {data["contact"]}")
    await state.clear()