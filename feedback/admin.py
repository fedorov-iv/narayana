# -*- coding: utf-8 -*-
from django.contrib import admin
from feedback.models import MailTemplate, Feedback, FeedbackSubject


class MailTemplatesAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    search_fields = ['title']

admin.site.register(MailTemplate, MailTemplatesAdmin)


class FeedbackSubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active', )
    list_editable = ('is_active', )

admin.site.register(FeedbackSubject, FeedbackSubjectAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('subject', 'create_date', 'email', 'is_answer_needed')
    list_filter = ['create_date', 'subject__title', 'is_answer_needed']
    search_fields = ['subject']
    readonly_fields = ['subject', 'user_name', 'email', 'body', 'create_date', 'is_answer_needed']

    def has_add_permission(self, request):
        return False

admin.site.register(Feedback, FeedbackAdmin)