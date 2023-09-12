from aiogram import types
from keyboards.reply_keyboard import main_keyboard
from keyboards.inline_keyboard import match_data_keyboard
from data_base.match_data import get_matches


async def start_command(message: types.Message):
    await message.answer(f"Hello {message.from_user.first_name}!", reply_markup=main_keyboard)

async def show_matches(message: types.Message):
    try:
        matches = get_matches()
    except:
        await message.answer(text="Дождитесь полного обновления матчей")
    for match in matches:
        await message.answer(f"""<b>{str(match[0])}</b>⚽️ против <b>{str(match[1])}</b>⚽️ 
Начало в <b>{match[2]}</b>🕚
{match[3]}
id матча 🆔: <b>{match[4]}</b>""", reply_markup=match_data_keyboard, parse_mode='HTML')