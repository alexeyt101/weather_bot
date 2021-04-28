import os
import logging

from dotenv import load_dotenv
from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

from handlers import greet_user
from weather import choose_airport, choose_weather_type, get_weather, weather_dontknow

load_dotenv()
logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    my_bot = Updater(os.getenv('API_KEY'), use_context=True)

    dp = my_bot.dispatcher

    weather = ConversationHandler(
            entry_points=[
                MessageHandler(Filters.regex('^(Получить погоду)$'), choose_weather_type)
            ],
            states={
                'choose_airport': [
                    MessageHandler(
                        Filters.regex('^(Текущая погода|Прогноз погоды)$'), choose_airport,
                        ),
                ],
                'get_weather': [MessageHandler(Filters.text, get_weather)]
            },
            fallbacks=[
                MessageHandler(
                    Filters.text | Filters.photo | Filters.document | Filters.video |
                    Filters.location, weather_dontknow
                )
            ]
        )

    dp.add_handler(weather)
    dp.add_handler(CommandHandler('start', greet_user))

    logging.info('Bot starts')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
