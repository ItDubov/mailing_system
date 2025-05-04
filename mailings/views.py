from django.shortcuts import render, redirect
from .models import Mailing
from .forms import MailingForm

def create_mailing(request):
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            mailing = form.save(commit=False)
            mailing.owner = request.user
            mailing.save()
            return redirect('mailing_list')
    else:
        form = MailingForm()
    return render(request, 'mailings/create_mailing.html', {'form': form})

def mailing_list(request):
    mailings = Mailing.objects.filter(owner=request.user)
    return render(request, 'mailings/mailing_list.html', {'mailings': mailings})
