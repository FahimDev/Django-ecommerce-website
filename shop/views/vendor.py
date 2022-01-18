from django.contrib.auth.models import Group
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages
from django.db import transaction
from django.contrib.auth import authenticate,login, logout
from shop.decorator import auth_user_page_restriction,allowed_user #Custom DesignPattern




from django.urls.conf import path
from shop.forms import CreateCategoryForm, CreateProductForm, AddProductImagesForm

from shop.models import Customer

def dashboard(request):
    context = {
        'title' : 'DAD',
    }

    return render(request, 'vendor/dashboard.html', context)

def createCategory(request):

    form = CreateCategoryForm
    context = {
        'title' : 'Create Category',
        'form' : form
    }

    if request.method == 'POST':
        form = CreateCategoryForm(request.POST,request.FILES)
        #address_form.initial['user'] = request.user.id
        
        print(form.errors)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'New Category Created')
                return redirect('add_category')
            except:
                messages.info(request, 'Something went wrong!')
                return redirect('add_category')

    return render(request, 'vendor/add_category.html', context)

def createProduct(request):

    form = CreateProductForm
    form_image = AddProductImagesForm
    context = {
        'title' : 'Create Product',
        'form' : form,
        'form_image' : form_image
    }

    if request.method == 'POST':
        form = CreateProductForm(request.POST,request.FILES)
        #address_form.initial['user'] = request.user.id
        
        print(form.errors)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'New Product Added')
                return redirect('add_product')
            except:
                messages.info(request, 'Something went wrong!')
                return redirect('add_product')

    return render(request, 'vendor/add_product.html', context)

def addProductPhotos(request):

    form_image = AddProductImagesForm
    context = {
        'title' : 'Product Photo',
        'form_image' : form_image
    }

    if request.method == 'POST':
        form_image = AddProductImagesForm(request.POST,request.FILES)
        
        print(form_image.errors)
        if form_image.is_valid():
            try:
                form_image.save()
                messages.success(request, 'New Product Image Added')
                return redirect('add_prod_photo')
            except Exception as e:
                messages.info(request, 'Something went wrong!')
                print(e)
                return redirect('add_prod_photo')

    return render(request, 'vendor/add_product_images.html', context)