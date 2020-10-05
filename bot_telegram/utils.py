from datetime import date
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings


def get_photo():
    photo_button = KeyboardButton('Send the photo')
    reply_keyboard = [[photo_button]]
    return reply_keyboard


def get_coordinates_button():
    location_button = KeyboardButton('Set coordinates', request_location=True, one_time_keyboard=True)
    reply_keyboard = [[location_button]]
    return reply_keyboard


def get_category_keyboard():
    reply_keyboard = [
                      ['Mark location as To Plant'], ['Mark location as a Stump'],
                      ['Mark location as Dead Tree'], ['Mark location as Dead Sapling']
                     ]
    return reply_keyboard
