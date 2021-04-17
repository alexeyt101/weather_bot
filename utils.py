import requests 

import config


def get_weather_data(url):
    try:
        weather_data = requests.get(url)
        weather_data.raise_for_status()
        return weather_data.text
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def process_weather_handlers(user_airport, weather_type):
    airport_code = config.airports_icao_codes.get(user_airport)
    if airport_code:
        weather_data = get_weather_data(
            config.BASE_URLS[weather_type].replace('<airport_ICAO_code>', airport_code)
        )
        if weather_data:
            answer_to_user = weather_data
        else:
            answer_to_user = 'Сервис погоды временно недоступен'
    else:
        answer_to_user = 'Не удалось определить ICAO-код аэропорта'
    return answer_to_user
