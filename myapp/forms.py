from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.IntegerField()

class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)