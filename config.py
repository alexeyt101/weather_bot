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

USER_EMOJI = [':sunglasses:', ':smiling_imp:', ':alien:']


KEYBOARDS = {
        'main': [['Получить погоду']],
        'weather_type': [['Текущая погода', 'Прогноз погоды']],
        'airports': [
            ['Шереметьево', 'Внуково'],
            ['Домодедово', 'Пулково']
        ],
    }
