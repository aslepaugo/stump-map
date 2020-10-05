from datetime import date
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         ConversationHandler)

from handlers import (reply_to_start_command, marking_point_dialog_start,
                     stop_the_program, marking_point_dialog_coordinates, marking_point_dialog_category)

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
            "select_category": [MessageHandler(
                Filters.regex('^(Mark location as To Plant|Mark location as a Stump|Mark location as Dead Tree|Mark location as Dead Sapling)$'),
                               marking_point_dialog_category)]      
        },
        fallbacks=[]
    )   

    dp.add_handler(mark_point_conversation) 
    dp.add_handler(CommandHandler("start", reply_to_start_command))
    dp.add_handler(MessageHandler(Filters.regex('^(Set location|Координаты места)$'), reply_to_start_command))
    dp.add_handler(CommandHandler("quit", stop_the_program))
    dp.add_handler(CommandHandler("exit", stop_the_program))
    #exit from bot is still not working

    mybot.start_polling()
    mybot.idle()
    

if __name__ == "__main__":
    main()