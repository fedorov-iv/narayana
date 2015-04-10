# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('',
    # список новостей
    url(r'^$', views.news_list, name='news_list'),
    url(r'^page/(?P<page>[1-9]\d*)/$', views.news_list, name='news_list'),
    # новость детально
    url(r'^(?P<news_id>[1-9]\d*)/$', views.news_detail, name='news_detail'),
)