from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.owner = request.user
            client.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/create_client.html', {'form': form})

def client_list(request):
    clients = Client.objects.filter(owner=request.user)
    return render(request, 'clients/client_list.html', {'clients': clients})