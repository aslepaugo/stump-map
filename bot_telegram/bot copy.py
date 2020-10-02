import logging, sys
import settings
from datetime import date
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


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
    dp.add_handler(CommandHandler("start", reply_to_start_command))
    dp.add_handler(CommandHandler("report", report_dialog))
    dp.add_handler(MessageHandler(Filters.regex('^(Координаты места)$'), report_dialog))
    dp.add_handler(CommandHandler("quit", stop_the_program))
    dp.add_handler(CommandHandler("exit", stop_the_program))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, report_dialog))

    mybot.start_polling()
    mybot.idle()
    

if __name__ == "__main__":
    main()