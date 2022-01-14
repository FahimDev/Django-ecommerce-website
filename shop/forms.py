from django.db import models
from django.db.models.fields import files
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

from shop.models import BillingAddress,Customer


class RegisterCustomerForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'username123'}))

    contact = forms.CharField(label='contact', widget=forms.NumberInput(attrs={'placeholder': '017XXXXXXXX'}))
    social_media_link = forms.CharField(label='Social Link', widget=forms.URLInput(attrs={'placeholder': 'https://www.facebook.com/example'}))


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','first_name', 'last_name', 'email', 'contact', 'social_media_link']

class UpdateCustomerForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CustomerInfoFrom(ModelForm):
    birthdate = forms.DateField(label='Birth Date', widget=forms.DateInput(attrs={'type': 'date'}))
    #profile_image = forms.ImageField(label='Profile Image', widget=forms.FileInput(attrs={'type': 'hidden','accept':'image/*'}))
    class Meta:
        model = Customer
        fields = ['social_media_link', 'gender', 'contact', 'profile_image', 'birthdate']

class BillingAddressForm(ModelForm):
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'rows': 3}))
    class Meta:
        model = BillingAddress
        fields = ['division', 'city', 'zip_code', 'address', 'user']
