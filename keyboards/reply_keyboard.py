from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Матчи⚽️"
        ),
        KeyboardButton(text="Обновить матчи🔄")
    ]
], resize_keyboard=True)