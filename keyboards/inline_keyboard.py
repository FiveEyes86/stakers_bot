from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

match_data_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Статистика 1 команды', callback_data='1_team_statistics'),
        InlineKeyboardButton(text='Статистика 2 команды', callback_data='2_team_statistics'),
    ],
    [
        InlineKeyboardButton(text='Прогноз', callback_data='prediction')
    ]
])

match_data_keyboard_activate = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Статистика 1 команды', callback_data='1_team_statistics'),
        InlineKeyboardButton(text='Статистика 2 команды', callback_data='2_team_statistics'),
    ],
    [
        InlineKeyboardButton(text='Прогноз', callback_data='prediction')
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data='back')
    ]
])