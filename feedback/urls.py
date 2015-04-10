# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from feedback import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='feedback'),
    url(r'^success/$', views.success, name='feedback_success'),
)
