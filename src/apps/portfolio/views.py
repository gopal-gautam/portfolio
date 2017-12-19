from collections import OrderedDict
from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.template.context_processors import csrf
from django.template.response import SimpleTemplateResponse
from django.views import View

from src.apps.usermessage.forms import UserMessageForm


class Index(View):
    def get(self, request):
        social = OrderedDict()
        social['facebook'] = 'https://fb.me/shirish.gautam'
        social['twitter'] = 'https://twitter.com/greatgopal'
        social['youtube'] = 'https://www.youtube.com/channel/UCkBfqMrltZmXtfLcSvo83Lw'
        social['github'] = 'https://github.com/shirish7151'
        social['instagram'] = 'https://www.instagram.com/sheereesh/'
        social['linkedin'] = 'https://www.linkedin.com/in/gopal-gautam-424829102/'
        social['stack-overflow'] = 'https://stackoverflow.com/users/6480218/gopal-gautam'

        top_skills = {'python': 80, 'django': 85, 'javascript': 80, 'css': 70}
        top_skills = OrderedDict(sorted(top_skills.items(), key=lambda x: x[1], reverse=True))
        context = {
            'fullname': 'Gopal Gautam',
            'profession': 'Web Developer & Software Engineer',
            'top_skills': top_skills,
            'socials': social,

            'user_message_form':UserMessageForm,
            'years_of_experience': relativedelta(datetime.now(), datetime.strptime('Sep 9 2014', '%b %d %Y')).years,
            'address': 'Kapan Budhanilkantha Municipality, Kathmandu Nepal',
            'phone': '+977 9841374658',
            'mail_address': 'gopal_007gautam@hotmail.com'
        }
        context.update(csrf(self.request))

        return SimpleTemplateResponse('index.html', context=context)
