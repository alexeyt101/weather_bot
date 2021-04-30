from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from utils import create_keyboard, process_weather_handlers

from config import AIRPORT_ICAO_CODES, KEYBOARDS


def choose_weather_type(update, context):
    update.message.reply_text(
        'Выберете вид погоды',
        reply_markup=create_keyboard('weather_type')
    )
    return 'choose_airport'


def choose_airport(update, context):
    user_weather_type = update.message.text
    if not user_weather_type or user_weather_type not in KEYBOARDS['weather_type'][0]:
        update.message.reply_text(
            'Выберите нужный тип погоды, используя клавиатуру',
            reply_markup=create_keyboard('weather_type')
        )
        return 'choose_airport'
 
    context.user_data['weather'] = {'weather_type': user_weather_type}
    update.message.reply_text(
        'Выберите ближайший аэропорт',
        reply_markup=create_keyboard('airports')
    )
    return 'get_weather'


def get_weather(update, context):
    weather_type = context.user_data['weather']['weather_type']
    airport_name = update.message.text.lower()
    if not airport_name or airport_name not in AIRPORT_ICAO_CODES.keys():
        update.message.reply_text(
            'Не удалось определить ICAO-код аэропорта',
            reply_markup=create_keyboard('airports')
        )
        return 'choose_airport'
    weather = process_weather_handlers(airport_name, weather_type)
    if weather:
        update.message.reply_text(
            weather,
            reply_markup=create_keyboard('main')
        )
        return ConversationHandler.END
    return 'get_weather'


def weather_dontknow(update, context):
    update.message.reply_text(
        'Я вас не понимаю, используйте клавиатуру',
        reply_markup=create_keyboard('weather_type')
        )
