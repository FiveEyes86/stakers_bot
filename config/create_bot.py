from aiogram import Bot, Dispatcher
from handlers.message_handlers import start_command, show_matches
from aiogram.filters import CommandStart
from handlers.callback_query_handlers import one_team_statistic, two_team_statistic, show_prediction, back
from aiogram import F
from launch import start_method, stop_method
from data_base.match_data import create_tables
from information_gathering.set_matches_data import get_matches_data


async def start_bot():
    bot = Bot('6456709156:AAFa89oEOxaWbH-VulWfgppuoSIPKXKfWsQ')
    dp = Dispatcher()

    dp.message.register(start_command, CommandStart())
    dp.message.register(show_matches, F.text == 'Матчи⚽️')
    dp.message.register(get_matches_data, F.text == 'Обновить матчи🔄')

    dp.callback_query.register(one_team_statistic, F.data.startswith('1_team_statistics'))
    dp.callback_query.register(two_team_statistic, F.data.startswith('2_team_statistics'))
    dp.callback_query.register(show_prediction, F.data.startswith('prediction'))
    dp.callback_query.register(back, F.data.startswith('back'))
    #dp.startup.register(start_method)
    #dp.shutdown.register(stop_method)
    create_tables()

    print("Start!")

    await dp.start_polling(bot)
