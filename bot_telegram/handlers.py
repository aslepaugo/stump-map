from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup
from telegram.ext import ConversationHandler
from keyboards import get_coordinates_button, get_category_keyboard

from services import save_coordinates, save_photo, save_category, send_photo, send_request
from categories import Categories

import logging
import os


def reply_to_start_command(update, context):
    text = 'Hi, in order to add a point, where you think it will be good, to plant a tree, please send a photo first'
    update.message.reply_text(text)    


def marking_point_dialog_start(update,context):
    logging.debug('Sent photo = called dialog')
    # save_photo(update, context)
    send_photo(update, context)

    update.message.reply_text(
        'Please share the location',
        reply_markup=ReplyKeyboardMarkup(keyboard=get_coordinates_button(),
                                         resize_keyboard=True))
    logging.debug('passing to the next step - Set coordinates')
    return 'set_coordinates'


def marking_point_dialog_coordinates(update, context):
    logging.debug('started step of marking point - marking_point_dialog_coordinates')
    coordinates = update.message.location

    update.message.reply_text(
        f'Your coordinates {coordinates}!',
        reply_markup=ReplyKeyboardMarkup(get_coordinates_button(),
        resize_keyboard=True)
    )
 
    save_coordinates(coordinates, context)
 
    update.message.reply_text(
        'Please select the category for the reported spot',
#        reply_markup=InlineKeyboardMarkup(inline_keyboard=get_category_keyboard()),
        reply_markup=InlineKeyboardMarkup(inline_keyboard=Categories.get_keyboard(),
                                            resize_keyboard=True))
    return 'select_category'


def marking_point_dialog_category(update, context):
    '''Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over'''
    query = update.callback_query
    query.answer()
    save_category(query.data, context)
    # coordinates = update.message.location
    # context.user_data['longitude'] = float(coordinates['longitude'])  
    # logging.info('Selected button ' + query.data)
    send_request(context)
    query.edit_message_text(
        text='Thank you, we will review this place and hope to hear from you soon.'
        )
    return ConversationHandler.END

