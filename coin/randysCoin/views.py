from django.shortcuts import render
from django.http import HttpResponse

import requests


def index(request):
    return render(request, "randysCoin/index.html")


def cryptos(request):
    response = requests.get("https://api.coincap.io/v2/assets").json()
    response = response["data"]
    return render(request, "randysCoin/cryptos.html", {"response": response})
