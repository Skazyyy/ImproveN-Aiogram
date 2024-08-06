from aiogram.types import ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Katalog")],  
                                    [KeyboardButton(text="Trash")],     
                                    [KeyboardButton(text="Contacts"),     
                                    KeyboardButton(text="What this")]],    
                                    resize_keyboard=True,
                                    input_field_placeholder="Выбери пункт меню...")


catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Futbolka")],
                                                [InlineKeyboardButton(text="krosowki")],
                                                [InlineKeyboardButton(text="Kepki")]])
