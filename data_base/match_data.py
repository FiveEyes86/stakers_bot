import sqlite3 as sq

def create_tables():
    global base
    global cur

    base = sq.connect('event_data.db')
    cur = base.cursor()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS team_one (command_wins INT,
                                                          command_goals INT,
                                                          command_average_goals FLOAT,
                                                          best_win VARCHAR(50),
                                                          count_games INT,
                                                          match_id INT
                                                        )""")

    cur.execute(f"""CREATE TABLE IF NOT EXISTS team_two (command_wins INT,
                                                          command_goals INT,
                                                          command_average_goals FLOAT,
                                                          best_win VARCHAR(50),
                                                          count_games INT,
                                                          match_id INT
                                                        )""")

    cur.execute(f"""CREATE TABLE IF NOT EXISTS matches (  command_one_name VARCHAR(50),
                                                          command_two_name VARCHAR(50),
                                                          start_match_time VARCHAR(50),
                                                          liga VARCHAR(50),
                                                          id INT
                                                        )""")

    base.commit()


def add_match(command_one_name, command_two_name, start_match_time, liga, id):
    cur.execute(f"""INSERT INTO matches (command_one_name, command_two_name, start_match_time, liga, id) VALUES
                    ("{command_one_name}", "{command_two_name}", "{start_match_time}", "{liga}", {id})""")
    base.commit()

def add_command_statistic(team_number, command_wins, command_goals, command_averge_goals, best_win, count_games, match_id):
    cur.execute(f"""INSERT INTO {team_number} (command_wins, command_goals, command_average_goals, best_win, count_games, match_id) VALUES
                    ({command_wins}, {command_goals}, {command_averge_goals}, "{best_win}", {count_games}, {match_id})""")

def get_matches():
    matches = list(cur.execute(f"""SELECT * FROM matches"""))
    return matches

def get_statistic(team_number, id):
    statistic = list(cur.execute(f"""SELECT * FROM {team_number} WHERE match_id = {id} """))
    return statistic

def get_team(team_number, id):
    command_name = cur.execute(f"""SELECT {str(team_number)} FROM matches WHERE id = {id}""").fetchall()
    return command_name

def get_match_data(id):
    data = list(cur.execute(f"""SELECT * FROM matches WHERE id = {id}"""))
    return data

def delete_data(table_name):
    cur.execute(f"""DELETE FROM {table_name}""")