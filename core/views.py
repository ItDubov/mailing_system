from django.shortcuts import render
from mailings.models import Mailing
from clients.models import Client
from mailings.models import MailingAttempt

def home(request):
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(status='started').count()
    unique_clients = Client.objects.count()

    return render(request, 'core/home.html', {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients
    })

def statistics(request):
    successful_attempts = MailingAttempt.objects.filter(status='success').count()
    failed_attempts = MailingAttempt.objects.filter(status='failed').count()
    total_sent = successful_attempts + failed_attempts

    return render(request, 'core/home.html', {
        'successful_attempts': successful_attempts,
        'failed_attempts': failed_attempts,
        'total_sent': total_sent
    })
