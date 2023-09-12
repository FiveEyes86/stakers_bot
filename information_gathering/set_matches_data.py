import requests, bs4, lxml
from data_base.match_data import add_match, add_command_statistic, delete_data
from aiogram import types, Bot

END_LINK = '&tab=stats_games'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': '*/*'
}

stake_information = requests.get('https://soccer365.ru/online/',

                     headers=HEADERS).text

HTML = bs4.BeautifulSoup(stake_information, 'lxml')

matches = list(HTML.find_all('div', class_='game_block'))

async def get_matches_data(message: types.Message, bot: Bot):

    mess = await message.answer(text="Идет сбор даных о матчах , подождите...")
    message_id = mess.message_id

    delete_data('matches')
    delete_data('team_one')
    delete_data('team_two')

    for match in matches:
        try:
            match_time = match.find('span', class_='size11').text
            game_link = match.find('a', class_='game_link')
            id = game_link.get('dt-id')

            resp = requests.get(f'https://soccer365.ru/games/{id}/{END_LINK}', headers=HEADERS).text
            HTML = bs4.BeautifulSoup(resp, 'lxml')
            try:
                command_one_data = list(HTML.find_all('div', class_='inf_vleft'))
                command_two_data = list(HTML.find_all('div', class_='inf_vright'))

                count_matches = int(HTML.find('div', class_='games_value').text)
                if (count_matches < 4):
                    continue

                command_one_wins = int(command_one_data[0].text)
                command_one_goals = int(command_one_data[1].text)
                command_one_average_goals = float(command_one_data[2].text)
                command_one_best_win = str(command_one_data[3].text)
                add_command_statistic('team_one', command_one_wins, command_one_goals, command_one_average_goals, command_one_best_win, count_matches, id)

                command_two_wins = int(command_two_data[0].text)
                command_two_goals = int(command_two_data[1].text)
                command_two_average_goals = float(command_two_data[2].text)
                command_two_best_win = str(command_two_data[3].text)
                add_command_statistic('team_two', command_two_wins, command_two_goals, command_two_average_goals, command_two_best_win, count_matches, id)
            except:
                continue
        except:
            continue
        commands = list(match.find_all('div', class_='img16'))
        command_one = commands[0].text
        command_two = commands[1].text
        liga = match.find('div', class_='stage').text

        add_match(command_one, command_two, match_time, liga, id)

    await bot.delete_message(message.chat.id, message_id)
    await message.answer(text="Матчи обновлены!")

