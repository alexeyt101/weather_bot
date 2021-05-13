BASE_URLS = {
    'Текущая погода': 'https://tgftp.nws.noaa.gov/data/observations/metar/stations/<airport_ICAO_code>.TXT',
    'Прогноз погоды': 'https://tgftp.nws.noaa.gov/data/forecasts/taf/stations/<airport_ICAO_code>.TXT'
}

AIRPORT_ICAO_CODES = {
    'шереметьево': 'UUEE',
    'домодедово': 'UUDD',
    'внуково': 'UUWW',
    'пулково': 'ULLI',
}

AIRPORTS_TIMEZONE = {
    'UTC+03': {
        'pytz_timezone': 'Europe/Moscow',
        'airports': ['шереметьево', 'домодедово', 'внуково', 'пулково'],
    },
}

USER_EMOJI = [':sunglasses:', ':smiling_imp:', ':alien:']


KEYBOARDS = {
        'main': [['Получить погоду']],
        'weather_type': [['Текущая погода', 'Прогноз погоды']],
        'airports': [
            ['Шереметьево', 'Внуково'],
            ['Домодедово', 'Пулково']
        ],
    }

USER_TIMEZONE = 'Europe/Moscow'