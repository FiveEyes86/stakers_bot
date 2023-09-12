import requests
import bs4, lxml

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': '*/*'
}

resp = requests.get('https://soccer365.ru/games/1929817/&tab=stats_games', headers=HEADERS).text
HTML = bs4.BeautifulSoup(resp, 'lxml')



try:
    command_one_data = list(HTML.find_all('div', class_='inf_vleft'))
    command_two_data =list(HTML.find_all('div', class_='inf_vright'))

    count_matches = int(HTML.find('div', class_='games_value').text)

    command_one_wins = int(command_one_data[0].text)
    command_two_wins = int(command_two_data[0].text)
    command_one_goals = int(command_one_data[1].text)
    command_two_goals = int(command_two_data[1].text)
    command_one_average_goals = float(command_one_data[2].text)
    command_two_average_goals = float(command_two_data[2].text)
    command_one_best_win = str(command_one_data[3].text)
    command_two_best_win = str(command_two_data[3].text)
    print(command_two_best_win, command_one_best_win, command_two_goals)
except:
    print("Не получилось собрать статистику")
