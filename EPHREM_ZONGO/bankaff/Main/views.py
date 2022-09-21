from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db import models
from .models import Agence
from .models import Client
from .models import Contact
from .forms import CreateContactForm




# Create your views here.
def home(request):
    return render(request, 'Main/home.html')
    
def agences(request):
    agences = Agence.objects.all()
    dictionnaire_agence = {
        'agence_key': agences
    }
    return render(request, 'Main/agences.html', dictionnaire_agence)

def clients(request):
    clients =  Client.objects.all()
    dictionnaire_client = {
        'client_key': clients
    }
    return render(request, 'Main/clients.html', dictionnaire_client)

def contact(request):
    form = CreateContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('home')
        else:            
            form = CreateContactForm()


    context = {'form': form}
    return render(request, 'Main/contact.html', context)







