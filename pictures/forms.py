from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to fill the form!')

        return cleaned_data

    def send_email(self):
        subject = 'subject'
        sender = self.cleaned_data['sender']
        message = "{name} / {email} said: ".format(
            name=self.cleaned_data.get('name'),
            email=self.cleaned_data.get('sender'))
        message += "\n\n{0}".format(self.cleaned_data.get('message'))
        recipients = [settings.ADMIN_EMAIL]
        send_mail(subject, message, sender, recipients, fail_silently=False)
