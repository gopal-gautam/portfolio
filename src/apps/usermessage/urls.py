from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^send_user_message/$', views.MailUserMessage.as_view(), name='mail-user-message'),
]