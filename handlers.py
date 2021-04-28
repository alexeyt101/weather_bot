from utils import create_main_keyboard, get_smile

def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f'Здравствуй, пользователь! {context.user_data["emoji"]}',
        reply_markup=create_main_keyboard()
    )