from random import choice

from emoji import emojize
import requests
import pytaf
from telegram import ReplyKeyboardMarkup

import config


def get_weather_data(url):
    try:
        weather_data = requests.get(url)
        weather_data.raise_for_status()
        return weather_data.text
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def parse_weather_data(weather_data):
    taf_position = weather_data.find('TAF')
    if taf_position >= 0:
        # weather_datetime = weather_data[:taf_position + 1]
        weather_data = weather_data[taf_position:].replace('\n', '')
    else:
        # weather_datetime = weather_data.split('\n')[0]
        weather_data = weather_data.split('\n')[1]
    t = pytaf.TAF(weather_data)
    d = pytaf.Decoder(t)
    decoded_weather = d.decode_taf()
    return decoded_weather


def process_weather_handlers(user_airport, weather_type):
    airport_code = config.airports_icao_codes.get(user_airport)
    if airport_code:
        weather_data = get_weather_data(
            config.BASE_URLS[weather_type].replace('<airport_ICAO_code>', airport_code)
        )
        if weather_data:
            weather_data = parse_weather_data(weather_data)
            answer_to_user = weather_data
        else:
            answer_to_user = 'Сервис погоды временно недоступен'
    else:
        answer_to_user = 'Не удалось определить ICAO-код аэропорта'
    return answer_to_user


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(config.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def create_main_keyboard():
    return ReplyKeyboardMarkup([['Текущая погода', 'Прогноз погоды']])