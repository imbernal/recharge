import requests


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def consuming(request):
    # r = requests.get('https://prod01.midas-card.com/plataforma/ws2/Balance.midas?parametros=/')
    return render(request, 'app/index.html')