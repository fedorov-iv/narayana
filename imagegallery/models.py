# -*- coding: utf8 -*-
from django.db import models
from ifcropper import ImageRatioField
from cms.models.pluginmodel import CMSPlugin
from imagegallery.admin_fields import *
from django.core.urlresolvers import reverse
from django.conf import settings


class Gallery(models.Model):
    """ Галерея """
    title = models.CharField(u'Название', max_length=256)
    create_date = models.DateField(u'Дата создания', default=datetime.date.today())
    preview_image = ImageRatioField('image', '221x100', verbose_name=u'Превью')
    image = models.ImageField(verbose_name=u'Изображение галереи', upload_to='imagegallery/images', blank=True)
    announce = models.TextField(u'Анонс', blank=True)
    detail = models.TextField(u'Описание', blank=True)
    order = models.PositiveIntegerField(u'Сортировка', default=0)
    is_active = models.BooleanField(u'Активность', default=1)

    #Укорачиваем анонс новости для списка
    def _short_announce(self):
        return short_announce(self.announce, 150)
    _short_announce.short_description = u'Анонс'
    _short_announce.allow_tags = True

    #Ссылка на картинки галереи
    def _show_galleryitems(self):
        url = reverse('admin:imagegallery_galleryitem_changelist') + '?gallery=' + str(self.pk)
        return '<a href="%s">=> К элементам галереи (%s)</a>' % (url, self.galleryitem_set.count())
    _show_galleryitems.allow_tags = True
    _show_galleryitems.short_description = u'Картинки'

    #Заголовок
    def __unicode__(self):
        return self.title

    #Задаём название приложения и сортировку
    class Meta:
        verbose_name = u'Галерея'
        verbose_name_plural = u'Галереи'
        ordering = ['-id']


class GalleryItem(models.Model):
    """ Изображение галереи """
    title = models.CharField(u'Название', max_length=256)
    preview_image = ImageRatioField('image', '221x100', verbose_name=u'Превью')
    image = models.ImageField(verbose_name=u'Изображение галереи', upload_to='imagegallery/images', blank=False)
    order = models.PositiveIntegerField(u'Сортировка', default=0)
    is_active = models.BooleanField(u'Активность', default=1)
    gallery = models.ForeignKey(Gallery, verbose_name=u'Галерея', blank=False)

    #Ссылка на картинки галереи
    def _show_preview(self):
        return '<img width="50px;" src="' + settings.MEDIA_URL + str(self.image) + '" />'
    _show_preview.allow_tags = True
    _show_preview.short_description = u'Превью'

    #Заголовок
    def __unicode__(self):
        return self.title

    #Задаём название приложения и сортировку
    class Meta:
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения'
        ordering = ['order']


class GalleryPlugin(CMSPlugin):
    gallery = models.ForeignKey(Gallery, verbose_name=u'Галерея', blank=False)