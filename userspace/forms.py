from django import forms
from userspace.models import MyUser

class create_user(forms.Form):
    username = forms.CharField(max_length=40)
    displayname = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)

class sign_in(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)