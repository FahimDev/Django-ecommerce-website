from django.db import models
from django.db.models.fields import files
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

from shop.models import BillingAddress, Category,Customer


from PIL import Image



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
        fields = ['division', 'city', 'zip_code', 'address', 'customer']


class CreateCategoryForm(ModelForm):
    category_name = forms.CharField(label='Category Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the category'}))
    unit = forms.CharField(label='Category Unit', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit of the category'}))
    small = forms.DecimalField(label='Small Quantity', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Size (small)'}))
    medium = forms.DecimalField(label='Medium Quantity', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Size (medium)'}))
    large = forms.DecimalField(label='Large Quantity', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Size (large)'}))
    policy = forms.CharField(label='Category Policy', widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))


    meta_keywords = forms.CharField(label='Meta Keywords (SEO)', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'keywords1, keywords2, keywords3,.........'}))
    meta_description = forms.CharField(label='Meta Description (SEO)', widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Write a short description about this category. (100 Words max)'}))
    slug = forms.CharField(label='Slug (URL-SEO)', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name-of-the-category'}))

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    image_width = forms.FloatField(widget=forms.HiddenInput())
    image_height = forms.FloatField(widget=forms.HiddenInput())
	
	
    #banner_img_path = forms.ImageField(label='Banner',required=False, widget=forms.FileInput(attrs={'class': 'form-control'})) #, initial='no'

    class Meta:
        model = Category
        fields = '__all__'

    def save(self):
        photo = super(CreateCategoryForm, self).save(commit=False)

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('image_width')
        h = self.cleaned_data.get('image_height')

        image = Image.open(photo.banner_img_path)
        print(x)
        cropped_image = image.crop((x, y, w + x, h + y))
        #resized_image = cropped_image.resize((117, 182), Image.ANTIALIAS) 
        cropped_image.save(photo.banner_img_path.path)
        return super(CreateCategoryForm, self).save(commit=True)
