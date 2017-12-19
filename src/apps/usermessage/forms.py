from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout, Field, Div
from django import forms

from crispy_forms.helper import FormHelper
from django.urls import reverse


class UserMessageForm(forms.Form):
    name = forms.CharField(label="Name", max_length=40, required=True)
    email = forms.EmailField(label="Email", max_length=40, required=True)
    message = forms.CharField(label="Message", max_length=800, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(UserMessageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'contactFrom'
        # self.helper.form_class = 'contactForm'
        self.helper.attrs = {'name': 'sentMessage', 'novalidate':'novalidate'}
        self.helper.form_show_labels = False
        self.helper.form_action = reverse('usermessage:mail-user-message')
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('name', placeholder='Name', id='name', template='field.html'),
                    css_class='col-md-6',
                ),
                Div(
                    Field('email', placeholder='Email', id='email', template='field.html'),
                    css_class='col-md-6',
                ),
                css_class='row'
            ),
            Field('message', rows='4', placeholder='Message', id='message', template='field.html'),
            StrictButton('Send Message', css_class='btn-default', type="submit")
        )