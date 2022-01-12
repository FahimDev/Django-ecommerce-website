from django.db import models
from django.db.models.fields import files
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from shop.models import BillingAddress,Product


class RegisterCustomer(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'username123'}))

    contact = forms.CharField(label='contact', widget=forms.NumberInput(attrs={'placeholder': '017XXXXXXXX'}))
    social_media_link = forms.CharField(label='Social Link', widget=forms.URLInput(attrs={'placeholder': 'https://www.facebook.com/example'}))


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','first_name', 'last_name', 'email', 'contact', 'social_media_link']

class BillingAddressCustomer(ModelForm):
    class Meta:
        model = BillingAddress
        fields = '__all__'
