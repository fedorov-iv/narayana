# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import *
from cms.models.pluginmodel import CMSPlugin
from tinymce import models as tinymce_models
import datetime


class News(models.Model):
    """ Новости """
    title = models.CharField(u'Название', max_length=255)
    create_date = models.DateTimeField(u'Дата создания', default=datetime.datetime.now())
    announce = models.TextField(u'Анонс', blank=True)
    detail = tinymce_models.HTMLField(u'Полный текст', blank=True)
    image = models.ImageField(verbose_name=u'Изображение ', upload_to='news/images', blank=True)
    is_active = models.BooleanField(u'Активность', default=1)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        ordering = ['-create_date', '-id']


class PageNews(CMSPlugin):
    """ CMS plugin: Новости главной страницы """
    per_page_count = models.PositiveIntegerField(u'Количество новостей на странице',
                                                 default=2,
                                                 validators=[MinValueValidator(1), MaxValueValidator(4)],
                                                 help_text=u'Кол-во новостей должно быть от 1 до 4')
