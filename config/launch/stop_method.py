from aiogram import Bot

async def stop_bot(bot: Bot):
    await bot.send_message(408910814, text="Бот остановлен!")
    print('Бот остановлен!')