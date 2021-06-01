from django import forms


class SearchForm(forms.Form):
    currency = forms.CharField(max_length=20)