from datetime import date
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import get_keyboard

from services import save_coordinates

import logging


def reply_to_start_command(update, context):
    text = "Привет, можешь мне прислать фотографию и координаты предпологаемого места, где нужно высадить дерево"
    update.message.reply_text(text, reply_markup=ReplyKeyboardMarkup(get_keyboard(), resize_keyboard=True))    


def report_dialog(update, context):
    logging.info("Called report")
    update.message.reply_text("Пошлите координаты точки, через контексное меню вашего мессенджера")
    

def user_coordinates(update, context):
    coordinates = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coordinates}!",
        reply_markup=ReplyKeyboardMarkup(get_keyboard(),
        resize_keyboard=True)
    )
    save_coordinates(coordinates)


def stop_the_program(update, context):
    #Still not working
    #logging.info("Called exit")
    #update.message.reply_text("Called quit, exiting the program")
    #update.stop()
    #update.is_idle = False
    pass
