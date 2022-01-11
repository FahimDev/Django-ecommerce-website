from django.contrib.auth.models import Group
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponseRedirect
from django.urls import reverse

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.urls.conf import path
from shop.forms import RegisterCustomer

from shop.models import Customer

def welcome(request):
    contex = {
        'title' : 'Home Page',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'class' : 'index-template fastfood_1'
    }
    return render(request,'welcome.html', contex)

def category(request):
    context = {
        'title' : 'Category Collections',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'class' : 'fastfood_1'
    }

    return render(request, 'category.html',context)

def categoryProducts(request):
    context = {
        'title' : 'Products by Category',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'class' : 'fastfood_1'
    }

    return render(request, 'category_products.html',context)

def details(request):
    context = {
        'title' : 'Product Detail',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'class' : 'fastfood_1'       
    }

    return render(request,'product_details.html',context)

def registration(request):
    form = RegisterCustomer
    context = {
        'title' : 'Registration | Customer',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'form_title' : 'Customer Registration',
        'class' : 'fastfood_1',  
        'form' : form
    }

    if request.method == 'POST':
        form = RegisterCustomer(request.POST)
        if form.is_valid():
            user = form.save()  #insert
            #Get contact number from form and store at phone 
            phone = form.cleaned_data.get('contact')
            #Get Social Link from form and store at link 
            link = form.cleaned_data.get('social_media_link')

            group = Group.objects.get(name='Customer')
            #insert Group type at auth_user_groups table
            user.groups.add(group)
            Customer.objects.create(contact = phone, social_media_link = link, user_id = user)
            return redirect('welcome')
    elif request.method == 'GET':
        return render(request, 'customer_registration.html', context)
    else:
        return HttpResponseRedirect(reverse('welcome'))