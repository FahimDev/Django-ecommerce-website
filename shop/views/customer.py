from django.contrib.auth import authenticate,login, logout
from shop.decorator import auth_user_page_restriction,allowed_user #Custom DesignPattern

from django.urls.conf import path
from shop.forms import BillingAddressCustomer

from shop.models import Customer

from django.contrib.auth.models import Group
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponseRedirect


@allowed_user
def profile(request):

    form = BillingAddressCustomer

    if request.method == 'POST':
        form = BillingAddressCustomer(request.POST)
        
        if form.is_valid():
            pass

    context = {
    'title' : 'Demo',
    'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
    'class' : 'fastfood_1',  
    'form' : form
    }
    return render(request, 'customer/profile.html', context)