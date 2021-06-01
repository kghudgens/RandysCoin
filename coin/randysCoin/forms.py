from django import forms


class SearchForm(forms.Form):
    currency = forms.CharField(label="Currency ID", max_length=20)