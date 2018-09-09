from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_celery(subject, sender, message, recipients):
    send_mail(subject, message, sender, recipients, fail_silently=False)
    return 'success'
