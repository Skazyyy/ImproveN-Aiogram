import asyncio
from aiogram import Dispatcher, F, Bot 
from app.handlers import router

bot = Bot(token="7370777292:AAGCdCu4CKzeh9hpFX6Q9V9d27U-5NBgsWs")
dp = Dispatcher()


async def main():
    bot = Bot(token="7370777292:AAGCdCu4CKzeh9hpFX6Q9V9d27U-5NBgsWs")
    dp = Dispatcher()
    dp.include_router(router) 
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Вырубил с вертухи бота")