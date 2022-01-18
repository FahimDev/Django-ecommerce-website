from django.db import models
from django.db.models.fields import files
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

from shop.models import BillingAddress, Category,Customer, Product, ProductImage


from PIL import Image
import os
from pprint import pprint


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

    x1 = forms.FloatField(widget=forms.HiddenInput())
    y1 = forms.FloatField(widget=forms.HiddenInput())
    image_width1 = forms.FloatField(widget=forms.HiddenInput())
    image_height1 = forms.FloatField(widget=forms.HiddenInput())
	
	
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

        x1 = self.cleaned_data.get('x1')
        y1 = self.cleaned_data.get('y1')
        w1 = self.cleaned_data.get('image_width1')
        h1 = self.cleaned_data.get('image_height1')

        image = Image.open(photo.banner_img_path)
       
        cropped_image = image.crop((x, y, w + x, h + y))
        c_path = photo.banner_img_path.path
        c_name = photo.banner_img_path
        cropped_image.save(c_path)
        photo.banner_img_path = c_name.name
        #pprint(c_name.name)

        #---------------------------------------------------------------------

        image1 = Image.open(photo.category_img_path)

        cropped_image1 = image1.crop((x1, y1, w1 + x1, h1 + y1))
        c_path1 = photo.category_img_path.path
        c_name1 = photo.category_img_path
        cropped_image1.save(c_path1) 
        photo.category_img_path = c_name1.name

        return super(CreateCategoryForm, self).save(commit=True)


#-------------------------------------------------------------------------------------------------

class CreateProductForm(ModelForm):
    product_title = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your product name'}))
    product_description = forms.CharField(label='Product Description', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3,'placeholder': 'Write a description about this product. (300 Words max)'}))
    video_url = forms.URLField(label='Video_URL', widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'www.example.com/demo/user'}))
    product_material = forms.CharField(label='Product Ingredients', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Mention the ingredients'}))
    product_brand = forms.CharField(label='Product Brand',required= False ,widget=forms.TextInput(attrs={'placeholder': 'Brand Name', 'class': 'form-control'}))
    product_sale = forms.DecimalField(label='Price Off' ,widget=forms.NumberInput(attrs={'placeholder': 'n < 100 (%)', 'class': 'form-control'}))
    price = forms.DecimalField(label='Product Price',widget=forms.NumberInput(attrs={'placeholder': 'Price of the Product (MRP in Taka)', 'class': 'form-control'}))


    meta_keywords = forms.CharField(label='Meta Keywords (SEO)', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'keywords1, keywords2, keywords3,.........'}))
    meta_description = forms.CharField(label='Meta Description (SEO)', widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Write a short description about this category. (100 Words max)'}))
    slug = forms.CharField(label='Slug (URL-SEO)', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name-of-the-category'}))


    class Meta:
        model = Product
        fields = '__all__'

    
#-------------------------------------------------------------------------------------------------

class AddProductImagesForm(ModelForm):

    img_title = forms.CharField(label='Image Title', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image title attribute is only visible on mouse hover'}))
    img_alt = forms.CharField(label='Alt text (SEO)', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Make sure all of your images include alt text (with relevant keywords included)'}))

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    image_width = forms.FloatField(widget=forms.HiddenInput())
    image_height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = ProductImage
        fields = '__all__'

    def save(self):
        photo = super(AddProductImagesForm, self).save(commit=False)

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('image_width')
        h = self.cleaned_data.get('image_height')

        image = Image.open(photo.product_img_src)
       
        cropped_image = image.crop((x, y, w + x, h + y))
        c_path = photo.product_img_src.path
        c_name = photo.product_img_src
        cropped_image.save(c_path)
        photo.product_img_src = c_name.name

        return super(AddProductImagesForm, self).save(commit=True)

