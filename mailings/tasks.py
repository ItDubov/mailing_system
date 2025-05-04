from django.core.mail import send_mail
from celery import shared_task
from .models import Mailing

@shared_task
def send_mail_task(mail_id):
    mailing = Mailing.objects.get(id=mail_id)
    for client in mailing.clients.all():
        send_mail(
            subject=mailing.message.subject,
            message=mailing.message.body,
            from_email='from@example.com',
            recipient_list=[client.email]
        )