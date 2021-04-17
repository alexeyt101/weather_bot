import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import config
from handlers import get_current_weather, get_weather_forecast, talk_to_me

logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    my_bot = Updater(config.API_KEY, use_context=True)

    dp = my_bot.dispatcher

    dp.add_handler(CommandHandler('weather', get_current_weather))
    dp.add_handler(CommandHandler('weather_forecast', get_weather_forecast))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot starts')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
