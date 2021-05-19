from datetime import datetime
import pytz
from random import choice

from emoji import emojize
import requests
import pytaf
from telegram import ReplyKeyboardMarkup

import config


def get_weather_data(url: str) -> str:
    """
    Функция, которая запрашивает данные у сервиса погоды и,
    в случае успеха, возвращает данные в текстовом виде
    """
    
    try:
        weather_data = requests.get(url)
        weather_data.raise_for_status()
        return weather_data.text
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def parse_weather_data(weather_data: str, user_airport: str) -> str:
    """
    Функция, которая принимает на вход строку погоды, полученную от сервиса погоды, 
    а также название аэропорта выбранного пользователем. 
    Возвращает очищенную от лишних пробелов и знаков переноса строку. 
    """
    
    weather_words_list = []
    weather_data = weather_data.replace('TAF', '').split('\n')
    weather_datetime_utc_timezone = datetime.strptime(weather_data[0], '%Y/%m/%d %H:%M')
    weather_datetime_airport_timezone = change_output_timezone(weather_datetime_utc_timezone, user_airport)
    # print(f'UTC: {weather_datetime_utc_timezone}\nUTC+3: {weather_datetime_airport_timezone}')
    weather_data = weather_data[1:]
    for row in weather_data:
        if not row:
            continue
        words_list = row.split()
        for word in words_list:
            if word:
                weather_words_list.append(word)
    weather_string_to_parse = ' '.join(weather_words_list)
    return weather_parsed_string


def change_output_timezone(datetime_utc: object, user_airport: str) -> object: 
    """
    Функция, которая принимает на вход объект datetime по UTC и
    название аэропорта, а возвращает объект datetime с timezone аэропорта.
    """
    
    airport_timezone = None
    utc_timezone = pytz.timezone('Etc/UTC')

    datetime_utc = utc_timezone.localize(datetime_utc)

    for timezone in config.AIRPORTS_TIMEZONE:
        if user_airport in config.AIRPORTS_TIMEZONE[timezone]['airports']:
            airport_timezone = config.AIRPORTS_TIMEZONE[timezone]['pytz_timezone']
    airport_timezone = pytz.timezone(airport_timezone)
    datetime_airport_timezone = datetime_utc.astimezone(airport_timezone)

    return datetime_airport_timezone


def process_weather_handlers(user_airport: str, weather_type: str) -> str:
    """
    Основная функция, которая принимает на вход название аэропорта и тип погоды,
    производит запрос погоды, обработку ответа, декодирование строки с погодой, возвращает
    ответ для пользователя (погода или сообщение об ошибке)
    """

    airport_code = config.AIRPORT_ICAO_CODES.get(user_airport)
    if airport_code:
        weather_data = get_weather_data(
            config.BASE_URLS[weather_type].replace('<airport_ICAO_code>', airport_code)
        )
        if weather_data:
            weather_string = parse_weather_data(weather_data, user_airport)
            weather_taf = pytaf.TAF(weather_string)
            weather_decoder = pytaf.Decoder(weather_taf)
            answer_to_user = weather_decoder.decode_taf()
        else:
            answer_to_user = 'Сервис погоды временно недоступен'
    else:
        answer_to_user = 'Не удалось определить ICAO-код аэропорта'
    return answer_to_user


def get_smile(user_data: dict) -> object:
    """
    Функция, которая возвращает смайлик для конкретного пользователя из user_data, если 
    его там нет, то выбирает случайный из имеющегося набора смайлов
    """

    if 'emoji' not in user_data:
        smile = choice(config.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def create_keyboard(keyboard_type):
    return ReplyKeyboardMarkup(
        config.KEYBOARDS.get(keyboard_type)
    )
