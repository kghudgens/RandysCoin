from django.shortcuts import render

# from django.shortcuts import redirect
from .forms import SearchForm

import requests


def index(request):
    return render(request, "randysCoin/index.html")


def cryptos(request):
    response = requests.get("https://api.coincap.io/v2/assets").json()
    response = response["data"]
    return render(request, "randysCoin/cryptos.html", {"response": response})


def search(request):
    form = SearchForm()
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            ID = form.cleaned_data["currency"]
            response = requests.get("https://api.coincap.io/v2/assets/" + ID).json()
            response = response["data"]
            return render(
                request, "randysCoin/search.html", {"form": form, "response": response}
            )
    else:
        form = SearchForm()
    return render(request, "randysCoin/search.html", {"form": form})
