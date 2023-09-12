from aiogram import Bot
from data_base.match_data import create_tables

async def start_bot(bot: Bot):
    create_tables()
    await bot.send_message(408910814, text="Бот запущен!")
    print("Бот запущен!")