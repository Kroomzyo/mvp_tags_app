import asyncio
import logging
from aiogram import Dispatcher
from config import settings
from config.bot_config import setup_bot, setup_dispatcher
from handlers import start_handler


async def main():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    bot = setup_bot()
    dp = setup_dispatcher()

    dp.include_router(start_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
