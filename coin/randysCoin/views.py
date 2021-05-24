from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

r = requests.get("https://api.coincap.io/v2/assets")
print(r.json())


def index(request):
    return render(request, "randysCoin/index.html")


def cryptos(request):
    return render(request, "randysCoin/cryptos.html")