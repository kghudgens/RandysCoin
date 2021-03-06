from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cryptos/", views.cryptos, name="cryptos"),
    path("search/", views.search, name="search"),
    path("contact/", views.contact, name="contact"),
]
