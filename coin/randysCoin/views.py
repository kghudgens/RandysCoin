from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "randysCoin/index.html")


def cryptos(request):
    return render(request, "randysCoin/cryptos.html")