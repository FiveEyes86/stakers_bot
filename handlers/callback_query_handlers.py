from aiogram.types import CallbackQuery
from data_base.match_data import get_statistic, get_team, get_match_data
from aiogram import Bot
from keyboards.inline_keyboard import match_data_keyboard, match_data_keyboard_activate

async def one_team_statistic(callback_data: CallbackQuery, bot: Bot):
    message_id = callback_data.message.message_id
    message = callback_data.message.text
    id = message[-7:]
    data = get_statistic('team_one', int(id))
    command_name = str(get_team('command_one_name', id))[3:-4]
    command_wins = data[0][0]
    command_goals = data[0][1]
    command_overage_goals = data[0][2]
    best_win = data[0][3]
    match_id = data[0][5]
    count_games = data[0][4]

    await bot.edit_message_text(chat_id=callback_data.message.chat.id, message_id=message_id, text=f"""Статистика <b>{str(command_name)}</b>⚽️:
Кол-во побед команды за последние <b>{str(count_games)}</b> матчей 🏆: <b>{str(command_wins)}</b>,
Кол-во голов команды за последние <b>{str(count_games)}</b> матчей 🥅: <b>{str(command_goals)}</b>,
Среднее кол-во голов команды за игру: <b>{str(command_overage_goals)}</b>,
Счет лучшего матча команды за последние игры 🥇: <b>{str(best_win)}</b>,
id матча 🆔: {str(match_id)}""", parse_mode='HTML', reply_markup=match_data_keyboard_activate)

async def two_team_statistic(callback_data: CallbackQuery, bot: Bot):
    message_id = callback_data.message.message_id
    message = callback_data.message.text
    id = message[-7:]
    command_name = str(get_team('command_two_name', id))[3:-4]
    data = get_statistic('team_two', int(id))
    command_wins = data[0][0]
    command_goals = data[0][1]
    command_overage_goals = data[0][2]
    best_win = data[0][3]
    match_id = data[0][5]
    count_games = data[0][4]

    await bot.edit_message_text(chat_id=callback_data.message.chat.id, message_id=message_id, text=f"""Статистика <b>{str(command_name)}</b>⚽️:
Кол-во побед команды за последние <b>{str(count_games)}</b> матчей 🏆: <b>{str(command_wins)}</b>,
Кол-во голов команды за последние <b>{str(count_games)}</b> матчей 🥅: <b>{str(command_goals)}</b>,
Среднее кол-во голов команды за игру: <b>{str(command_overage_goals)}</b>,
Счет лучшего матча команды за последние игры 🥇: <b>{str(best_win)}</b>,
id матча 🆔: {str(match_id)}""", parse_mode='HTML', reply_markup=match_data_keyboard_activate)


# POV - probability of victory
async def show_prediction(callback_data: CallbackQuery, bot: Bot):
    message_id = callback_data.message.message_id
    message = callback_data.message.text
    id = message[-7:]
    team_one = get_statistic('team_one', int(id))
    team_two = get_statistic('team_two', int(id))

    team_one_name = str(get_team('command_one_name', id))[3:-4]
    team_two_name = str(get_team('command_two_name', id))[3:-4]

    POV_team_one = team_one[0][0] / team_one[0][4] * 100
    POV_team_two = team_two[0][0] / team_two[0][4] * 100
    POV_equal_score = (team_one[0][4] - (team_one[0][0] + team_two[0][0])) / team_two[0][4] * 100
    total_team_one = team_one[0][2]
    total_team_two = team_two[0][2]
    total = team_one[0][2] + team_two[0][2]

    match_id = team_one[0][5]

    await bot.edit_message_text(chat_id=callback_data.message.chat.id, message_id=message_id, text=f"""Вероятность победы <b>{team_one_name}: {round(POV_team_one, 2)}%</b>,
Вероятность победы <b>{team_two_name}: {round(POV_team_two, 2)}%</b>,
Вероятность <b>ничьей: {round(POV_equal_score, 2)}%</b>,
Средний тотал {team_one_name}: <b>{round(total_team_one, 2)}</b>,
Средний тотал {team_two_name}: <b>{round(total_team_two, 2)}</b>,
Средний тотал всего матча: <b>{round(total, 2)}</b>,
id матча: {str(match_id)}""", parse_mode='HTML', reply_markup=match_data_keyboard_activate)


async def back(callback_data: CallbackQuery, bot: Bot):
    message_id = callback_data.message.message_id
    message = callback_data.message.text
    id = message[-7:]
    match_data = get_match_data(id)
    await bot.edit_message_text(chat_id=callback_data.message.chat.id, message_id=message_id, text=f"""<b>{str(match_data[0][0])}</b>⚽️ против <b>{str(match_data[0][1])}</b>⚽️  
    Начало в <b>{match_data[0][2]}</b>🕚
    {match_data[0][3]}
    id матча 🆔: <b>{match_data[0][4]}</b>""", reply_markup=match_data_keyboard, parse_mode='HTML')

