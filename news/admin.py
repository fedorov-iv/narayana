# -*- coding: utf-8 -*-
from news.models import News
from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin


class NewsAdmin(MCEFilebrowserAdmin):
    """ Новости """
    list_display = ('title', 'create_date', 'is_active')
    list_filter = ['is_active']
    date_hierarchy = 'create_date'
    search_fields = ['title', 'detail']
    list_editable = ['is_active']

admin.site.register(News, NewsAdmin)


