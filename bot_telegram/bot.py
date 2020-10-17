from datetime import date
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         ConversationHandler,CallbackQueryHandler)

from handlers import (reply_to_start_command, marking_point_dialog_start,
                     marking_point_dialog_coordinates, marking_point_dialog_category)

from categories import Categories

import logging, sys
import settings


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher

    mark_point_conversation = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.photo, marking_point_dialog_start)
        ],
        states={
            "set_coordinates": [MessageHandler(Filters.location, marking_point_dialog_coordinates)],
            "select_category": [
                    #it is very possible, that there is no need to catch something in particulary here.
                    # CallbackQueryHandler(marking_point_dialog_category, pattern='^' + 'b_missing_tree' + '$'),
                    # CallbackQueryHandler(marking_point_dialog_category, pattern='^' + 'b_stump' + '$'),                
                    # CallbackQueryHandler(marking_point_dialog_category, pattern='^' + 'b_dead_tree' + '$'),
                    # CallbackQueryHandler(marking_point_dialog_category, pattern='^' + 'b_dead_sapling' + '$')
                    CallbackQueryHandler(marking_point_dialog_category, pattern=Categories.get_pattern())                
                                ]      
               },
        fallbacks=[]
    )   

    dp.add_handler(mark_point_conversation) 
    dp.add_handler(CommandHandler("start", reply_to_start_command))
    dp.add_handler(MessageHandler(Filters.regex('^(Set location|Координаты места)$'), reply_to_start_command))

    mybot.start_polling()
    mybot.idle()
    

if __name__ == "__main__":
    main()