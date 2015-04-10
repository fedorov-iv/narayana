# -*- coding: utf8 -*-

"""
Сборник административных полей
"""

from django.conf import settings
import datetime


def show_period(date_from, date_to):
    """ Указывает корректный период показа """
    if date_from and date_to:
        return '%s - %s' % (date_from, date_to)
    elif date_from and not date_to:
        return 'от %s' % (date_from)
    elif not date_from and date_to:
        return 'до %s' % (date_to)
    else:
        return 'всегда'


def show_period_icon(date_from, date_to, is_active):
    """ Учитывает активность объекта и период показа и возвращает корректную иконку """
    
    static_files_url = settings.STATIC_URL

    if not is_active:
        return '<img src="%simg/icons/admin/icon-no.gif" alt="Отключена">' % (static_files_url)
    else:
        current_date = datetime.date.today()
        if date_from and date_to:
            if date_from > current_date or current_date > date_to:
                return '<img src="%simg/icons/admin/icon_alert.gif" alt="Новость вне периода показа">' % (static_files_url)
            else:
                return '<img src="%simg/icons/admin/icon-yes.gif" alt="Активна">' % (static_files_url)
        elif date_from and not date_to:
            if date_from > current_date:
                return '<img src="%simg/icons/admin/icon_alert.gif" alt="Новость вне периода показа">' % (static_files_url)
            else:
                return '<img src="%simg/icons/admin/icon-yes.gif" alt="Активна">' % (static_files_url)
        elif not date_from and date_to:
            if current_date > date_to:
                return '<img src="%simg/icons/admin/icon_alert.gif" alt="Новость вне периода показа">' % (static_files_url)
            else:
                return '<img src="%simg/icons/admin/icon-yes.gif" alt="Активна">' % (static_files_url)
        else:
            return '<img src="%simg/icons/admin/icon-yes.gif" alt="Активна">' % (static_files_url)


def short_announce(announce, length):
    """ Показывает укороченный анонс, корректно отображающий html-теги """
    if len(announce)>length:
        return '<div title="'+announce+'">'+announce[:length-3]+'...'+'</div>'
    else:
        return '<div title="'+announce+'">'+announce+'</div>'