from django.shortcuts import render
from django.http import HttpRequest

def welcome(request):
    contex = {
        'title' : 'Home Page',
        'class' : 'index-template fastfood_1'
    }
    return render(request,'welcome.html', contex)

def category(request):
    context = {
        'title' : 'Category Collections',
        'class' : 'fastfood_1'
    }

    return render(request, 'category.html',context)

def categoryProducts(request):
    context = {
        'title' : 'Products by Category',
        'class' : 'fastfood_1'
    }

    return render(request, 'category_products.html',context)

def details(request):
    context = {
        'title' : 'Product Detail',
        'class' : 'fastfood_1'       
    }

    return render(request,'product_details.html',context)

def registration(request):
    context = {
        'title' : 'Registration | Customer',
        'class' : 'fastfood_1'  
    }

    return render(request, 'customer_registration.html', context)