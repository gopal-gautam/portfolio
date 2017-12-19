from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin, FormView

from src.apps.usermessage.forms import UserMessageForm

from django.conf import settings

from mailer import send_mail as send_mail_db

# if "mailer" in settings.INSTALLED_APPS:
#     from mailer import send_mail
# else:
#     from django.core.mail import send_mail


class MailUserMessage(FormView, FormMixin):
    form_class = UserMessageForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        subject = 'New message for gopalgautam from %s' %(form.cleaned_data.get('name'))
        body = 'New message received from email: %s as: %s' %(form.cleaned_data.get('email'), form.cleaned_data.get('message'))
        # send_mail('Sent django', 'Django mail message body', 'gopalgautam.mailgateway@gmail.com', ['gopal.007gautam@gmail.com'])
        recipients = ['gopal.007gautam@gmail.com']
        email = EmailMessage(subject, body, to=recipients)
        sent_status = email.send()
        send_mail_db(subject, body, settings.DEFAULT_FROM_EMAIL, recipients)
        return HttpResponse("Success", status=200)

