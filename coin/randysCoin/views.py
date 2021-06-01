from django.shortcuts import render
from .forms import SearchForm

import requests


def index(request):
    """View for the home page"""
    return render(request, "randysCoin/index.html")


def cryptos(request):
    """View for the crypto page, showing the top 12 cryptos"""
    # store get method in the response variable
    response = requests.get("https://api.coincap.io/v2/assets").json()
    # Parse the saved json object with the data key
    response = response["data"]
    return render(request, "randysCoin/cryptos.html", {"response": response})


def search(request):
    """View for the search page"""
    # instantiate the form
    form = SearchForm()
    if request.method == "GET":
        form = SearchForm(request.GET)
        # if proper data is entered in the form perform the following actions
        if form.is_valid():
            # Get the input entered in the search form
            ID = form.cleaned_data["currency"]
            # take the users input and concatenate to the end of the get method to get whats requested
            response = requests.get("https://api.coincap.io/v2/assets/" + ID).json()
            # Parse the json method
            response = response["data"]
            return render(
                request, "randysCoin/search.html", {"form": form, "response": response}
            )
    else:
        form = SearchForm()
    return render(request, "randysCoin/search.html", {"form": form})
