from utils import process_weather_handlers


def get_current_weather(update, context):
    user_airport = update.message.text.split()[1].lower()
    answer_to_user = process_weather_handlers(user_airport, 'current_weather')
    update.message.reply_text(answer_to_user)


def get_weather_forecast(update, context):
    user_airport = update.message.text.split()[1].lower()
    answer_to_user = process_weather_handlers(user_airport, 'weather_forecast')
    update.message.reply_text(answer_to_user)


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)
