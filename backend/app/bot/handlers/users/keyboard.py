from telebot.types import Message

from ...loader import bot
from ...base import base
from ...keyboards.default import get_menu_keyboard_markup, get_remove_keyboard_markup
from ...utils import send_message_private

from app.models import User


@bot.message_handler(commands=['keyboard'])
@base()
def keyboard_handler(message: Message, current_user: User):
    text = 'Выберите действие в меню. 👇'

    send_message_private(message, text, reply_markup=get_menu_keyboard_markup(current_user.is_admin()))


@bot.message_handler(commands=['keyboard_off'])
@base()
def keyboard_off_handler(message: Message, current_user: User):
    text = 'Меню отключено. ❌'

    send_message_private(message, text, reply_markup=get_remove_keyboard_markup())

