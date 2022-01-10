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