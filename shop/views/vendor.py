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

def dashboard(request):
    context = {
        'title' : 'DAD',
    }

    return render(request, 'vendor/dashboard.html', context)

def createCategory(request):
    context = {
        'title' : 'Create Category',
    }

    return render(request, 'vendor/add_category.html', context)