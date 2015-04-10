# -*- coding: utf-8 -*-
from django.db import models
import datetime
from tinymce import models as tinymce_models
from django.forms import ValidationError


class MailTemplate(models.Model):
    title = models.CharField(u'Название', max_length=255)
    code = models.CharField(u'Символьный код', max_length=255, unique=True)
    from_name = models.CharField(u'От (имя)', max_length=255)
    from_email = models.EmailField(u'От (e-mail)', max_length=255)
    admin_email = models.EmailField(u'Кому (e-mail)', max_length=255)
    copy_emails = models.EmailField(u'Копия (e-mail)', max_length=255, blank=True)
    subject = models.CharField(u'Тема сообщения', max_length=255)
    body = tinymce_models.HTMLField(u'Текст сообщения', blank=True)

    class Meta:
        verbose_name = u'почтовый шаблон'
        verbose_name_plural = u'почтовые шаблоны'
        ordering = ['id']

    def __unicode__(self):
        return self.title


class FeedbackSubject(models.Model):
    title = models.CharField(u'Тема', max_length=255)
    is_active = models.BooleanField(u'Активность', default=True)

    class Meta:
        verbose_name = u'тема обращения'
        verbose_name_plural = u'темы обращений'
        ordering = ['id']

    def __unicode__(self):
        return self.title


class Feedback(models.Model):
    user_name = models.CharField(u'Имя пользователя', max_length=255)
    subject = models.ForeignKey(FeedbackSubject, verbose_name=u'Тема', limit_choices_to={'is_active':True})
    email = models.EmailField(u'E-mail')
    body = models.TextField(u'Текст обращения')
    is_answer_needed = models.BooleanField(u'Требует ответа', default=False, blank=True)
    create_date = models.DateTimeField(u'Дата создания', default=datetime.datetime.now())

    class Meta:
        verbose_name = u'обращение пользователя'
        verbose_name_plural = u'обращения пользователей'
        ordering = ['-create_date', '-id']

    def __unicode__(self):
        return self.body