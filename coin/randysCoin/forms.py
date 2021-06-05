from django import forms


class SearchForm(forms.Form):
    currency = forms.CharField(max_length=20)


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.TextInput()