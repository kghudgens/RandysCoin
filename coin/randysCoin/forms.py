from django import forms
from django.forms import ModelForm
from .models import Contact


class SearchForm(forms.Form):
    currency = forms.CharField(max_length=20)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email", "subject"]
