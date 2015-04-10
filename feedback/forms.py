# -*- coding: utf-8 -*-
from feedback.models import Feedback, FeedbackSubject
from django import forms
from captcha.fields import CaptchaField


class FeedbackForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Feedback
        exclude = ['create_date']
        #fields = ['active_subjects', 'body', 'email']
