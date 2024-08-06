from aiogram.types import ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Katalog")],  
                                    [KeyboardButton(text="Trash")],     
                                    [KeyboardButton(text="Contacts"),     
                                    KeyboardButton(text="What this")]],    
                            resize_keyboard=True,
                            input_field_placeholder="Выбери пункт меню...")


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Futbolka", callback_data="Футболка")],
    [InlineKeyboardButton(text="krosowki", callback_data="Кросовки")],
    [InlineKeyboardButton(text="Kepki", callback_data="Кепки")]])


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить номер", 
                                                           request_contact=True)]],
                                resize_keyboard=True)