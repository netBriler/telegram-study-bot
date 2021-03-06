from app.models import Subject
from app.services.subjects import get_all_subjects
from telebot import types


def get_subjects_inline_markup(query: str):
    markup = types.InlineKeyboardMarkup()
    subjects = get_all_subjects()
    for s in range(int(len(subjects) / 2)):
        s *= 2
        btn = types.InlineKeyboardButton(subjects[s].name, callback_data=f'{query}_{subjects[s].codename}')
        btn2 = types.InlineKeyboardButton(subjects[s + 1].name, callback_data=f'{query}_{subjects[s + 1].codename}')
        markup.row(btn, btn2)
    if len(subjects) % 2:
        markup.add(types.InlineKeyboardButton(subjects[-1].name, callback_data=f'{query}_{subjects[-1].codename}'))
    markup.row(types.InlineKeyboardButton('❌Отменить❌', callback_data=f'{query}_cancel'))
    return markup


def get_subject_files_inline_markup(subject: Subject):
    markup = types.InlineKeyboardMarkup()

    for file in subject.files:
        markup.row(types.InlineKeyboardButton(file.title, callback_data=f'file_{file.id}'))

    return markup
