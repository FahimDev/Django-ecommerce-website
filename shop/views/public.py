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
from shop.forms import RegisterCustomerForm

from shop.models import Customer

def welcome(request):
    contex = {
        'title' : 'Home Page',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'class' : 'index-template fastfood_1',
        #------Content For Welcome Page------
        'welcopme_caption' : 'Biryani is Love!', #h2 tag
        'welcome_story' : 'Biryani is a mixed rice dish originating among the Bangalis. It is made with spices, rice, and meat, and sometimes, in addition, eggs and/or vegetables. Biryani is popular throughout the Bangladesh, as well as among its diaspora.',
        'welcome_image_name' : 'popup-foodCover.png',
        'banner_title' : 'Free!',
        'banner_caption' : 'Home Delivery',
        'hover_deal' : 'hoverFoodDeal.png'
    }
    return render(request,'visitors/welcome.html', contex)


def category(request):
    context = {
        'title' : 'Category Collections',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'class' : 'fastfood_1'
    }

    return render(request, 'visitors/category.html',context)

def categoryProducts(request):
    context = {
        'title' : 'Products by Category',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'class' : 'fastfood_1'
    }

    return render(request, 'visitors/category_products.html',context)

def details(request):
    context = {
        'title' : 'Product Detail',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'class' : 'fastfood_1'       
    }

    return render(request,'visitors/product_details.html',context)


@auth_user_page_restriction
def registration(request):
    form = RegisterCustomerForm

    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        
        if form.is_valid():
            #Transaction is a very impornt module in Django ORM. Here multiple operation will take place in different table. This module will ensure none of those will not get miss 
            with transaction.atomic():
                user = form.save()  #Insert / Update
                #Get contact number from form and store at phone 
                phone = form.cleaned_data.get('contact')
                #Get Social Link from form and store at link 
                link = form.cleaned_data.get('social_media_link')

                group = Group.objects.get(name='Customer')
                #insert Group type at auth_user_groups table
                user.groups.add(group)
                Customer.objects.create(contact = phone, social_media_link = link, user = user)

                messages.success(request, 'New User Created Successfully')

                return redirect('login')
    context = {
    'title' : 'Registration | Customer',
    'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
    'form_title' : 'Customer Registration',
    'class' : 'fastfood_1',  
    'form' : form
    }
    return render(request, 'visitors/customer_registration.html', context)

@auth_user_page_restriction
def loginPage(request):
    context = {
    'title' : 'Login | User',
    'form_title' : 'Customer Registration',
    'class' : 'fastfood_1',  
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('unlock')
        else:
            messages.info(request, 'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.')
            return render(request, 'login.html', context)

    return render(request, 'visitors/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('welcome')

def error(request,exception=None):
    context = {
        'title' : '404',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'class' : 'fastfood_1',  

        'caption': 'Oh my gosh! you found it !!!',
        'sub_text': 'Looks like the page you are trying to visit does not exist. Please check the URL and try your lick again'
    }

    return render(request, 'visitors/404.html', context)


@allowed_user
def unlock(request):
    return redirect('cus_profile')

def demo(request):
    pass