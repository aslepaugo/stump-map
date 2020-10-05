#from datetime import date
from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import get_coordinates_button, get_category_keyboard, get_photo

from services import save_coordinates, save_photo, save_category

import logging
import os


def reply_to_start_command(update, context):
    text = 'Hi, in order to add a point, where you think it will be good, to plant a tree, please send a photo first'
    update.message.reply_text(text)    


def marking_point_dialog_start(update,context):
    logging.debug("Sent photo = called dialog")
    save_photo(update, context)
    update.message.reply_text(
        'Please share the location',
        reply_markup=ReplyKeyboardMarkup(keyboard=get_coordinates_button()),
        resize_keyboard=True)
    logging.debug("passing to the next step - Set coordinates")
    return "set_coordinates"


def marking_point_dialog_coordinates(update, context):
    logging.debug("started step of marking point - marking_point_dialog_coordinates")
    coordinates = update.message.location
    update.message.reply_text(
        f'Your coordinates {coordinates}!',
        reply_markup=ReplyKeyboardMarkup(get_coordinates_button(),
        resize_keyboard=True)
    )
    save_coordinates(coordinates)
    update.message.reply_text(
        'Please select the category for the reported spot',
        reply_markup=ReplyKeyboardMarkup(keyboard=get_category_keyboard()),
        resize_keyboard=True)
    return "select_category"


def marking_point_dialog_category(update, context):
    save_category(update.message.text)
    update.message.reply_text(
        "Thank you, we will review this place and hope to hear from you soon again.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def stop_the_program(update, context):
    #Still not working
    #logging.info('Called exit')
    #update.message.reply_text('Called quit, exiting the program')
    #update.stop()
    #update.is_idle = False
    pass
