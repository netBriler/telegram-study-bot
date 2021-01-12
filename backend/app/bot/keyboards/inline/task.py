import telebot
from telebot import types


def get_edit_inline_markup(query: str, id: int):
    query = query + str(id)
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('🛠️Редактировать🛠️', callback_data=query + '_edit'),
               types.InlineKeyboardButton('☢Удалить☢', callback_data=query + '_delete'))

    markup.row(types.InlineKeyboardButton('❌Отменить❌', callback_data=query + '_cancel'))
    return markup
