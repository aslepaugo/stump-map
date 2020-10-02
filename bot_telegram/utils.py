from datetime import date
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings


def get_keyboard():
    location_button = KeyboardButton('Координаты места', request_location=True)
    reply_keyboard = [['Прислать фотографию места для высадки дерева'], [location_button]]
    return reply_keyboard
    
