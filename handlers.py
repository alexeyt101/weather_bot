from utils import create_keyboard, get_smile


def greet_user(update, context):
    """
    Функция, которая отправляет пользователю приветственную фразу с 
    смайликом
    """

    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f'Здравствуй, пользователь! {context.user_data["emoji"]}',
        reply_markup=create_keyboard('main')
    )
