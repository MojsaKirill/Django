from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.IntegerField()

class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()