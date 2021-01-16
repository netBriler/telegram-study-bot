from telebot.types import Message

from ...loader import bot
from ...base import base

from app.models import User


@bot.message_handler(regexp='^🆘Помощь🆘$')
@bot.message_handler(commands=['help'])
@base()
def help_handler(message: Message, current_user: User):
    text = """    
🆘 Информация 🆘

/info - Узнать информацию по предмету
/schedule - Узнать расписание
/homework - Узнать ДЗ

/help - Помощь по боту
/keyboard - Подключить клавиатуру
/keyboard_off - Отключить клавиатуру
"""
    if current_user.is_admin():
        text += """
👑 Информация для администраторов 👑

<i>ДЗ можно добавлять по быстрому шаблону</i>
<pre>!Название предмета - задание</pre>

/add - Добавить ДЗ
/edit - Изменить ДЗ

/get_id - Получить id сообщения (id прийдет в личку)
/get_file_id - Получить id файла
/delete - Удалить сообщение бота
/call_all - Позвать всех участников группы
"""

    text += """
Создатель @briler
"""

    bot.send_message(message.chat.id, text)

