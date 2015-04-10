# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from feedback.forms import FeedbackForm
from feedback.models import MailTemplate
from django.core.mail import EmailMessage
from django.contrib import messages
import datetime
from django.utils.translation import ugettext as _


def index(request):

    if request.method == 'POST':

        f = FeedbackForm(data=request.POST)
        if f.is_valid():
            f.instance.create_date = datetime.datetime.now()
            f.save()

            mail_template = MailTemplate.objects.get(code__exact='FEEDBACK')
            body = mail_template.body.replace('###hostname###', request.get_host())
            body = body.replace('###email###', f.instance.email)
            body = body.replace('###user_name###', f.instance.user_name)
            body = body.replace('###subject###', f.instance.subject.title)
            body = body.replace('###body###', f.instance.body)
            body = body.replace('###is_answer_needed###', u'Да' if f.instance.is_answer_needed else u'Нет')

            email = EmailMessage(
                mail_template.subject,
                body,
                mail_template.from_email,
                [mail_template.admin_email, ],
                [mail_template.copy_emails, ],
                headers={'Reply-To': mail_template.from_email, 'From': mail_template.from_name}
            )

            email.content_subtype = "html"
            email.send()
            messages.add_message(request, messages.SUCCESS, _("Message sent successfully!"))
            return redirect('feedback_success')

    else:
        f = FeedbackForm()

    return render(request, 'feedback/index.html', {'form': f})


def success(request):
    return render(request, 'feedback/success.html')