from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SearchForm, ContactForm


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


def contact(request):
    """View for the contact page"""
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data["first_name"] + form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["subject"]
            send_mail(
                "Randy's Coin Contact",
                message,
                email,
                ["hudgens1073@gmail.com"],
                fail_silently=False,
            )
            None
    else:
        form = ContactForm()
    return render(request, "randysCoin/contact.html")
