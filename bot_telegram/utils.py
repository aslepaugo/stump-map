from datetime import date
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

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
    inline_keyboard = [
                      [InlineKeyboardButton('Mark location as To Plant', callback_data='b_missing_tree')],
                      [InlineKeyboardButton('Mark location as a Stump', callback_data='b_stump')],
                      [InlineKeyboardButton('Mark location as Dead Tree', callback_data='b_dead_tree')],
                      [InlineKeyboardButton('Mark location as Dead Sapling', callback_data='b_dead_sapling')]
                      # Макс можно ли тут вызвать что-то типа
                      #[InlineKeyboardButton(someobject.lable, callback_data=someobject.lable.group_name)] 
                      # чтобы все эти перевороты из группы в лейбл и обратно иметь в чем-то отдельном
                     ]
    #reply_keyboard = [
    #                  ['Mark location as To Plant'], ['Mark location as a Stump'],
    #                  ['Mark location as Dead Tree'], ['Mark location as Dead Sapling']
    #                 ]
    return inline_keyboard
