# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from news.models import PageNews, News


class MainPageNewsPlugin(CMSPluginBase):
    """ Плагин: вывод 'n' новостей (специально для главной страницы) """
    model = PageNews
    name = u'Новости для главной страницы'
    render_template = u"news/plugins/main_page_news.html"

    def render(self, context, instance, placeholder):
        context['count'] = News.objects.filter(is_active=True).count()
        news_list = News.objects.filter(is_active=True)[:instance.per_page_count]
        context['news_list'] = news_list
        return context

plugin_pool.register_plugin(MainPageNewsPlugin)
