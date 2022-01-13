from django.contrib.auth import authenticate,login, logout
from shop.decorator import auth_user_page_restriction,allowed_user #Custom DesignPattern

from django.urls.conf import path
from django.contrib.auth.models import Group
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponseRedirect

from shop.forms import BillingAddressForm,UpdateCustomerForm,CustomerInfoFrom

from shop.models import Customer


@allowed_user
def profile(request):
    customer_info = Customer.objects.get(user_id = request.user.id)

    form = BillingAddressForm

    if request.method == 'POST':
        form = BillingAddressForm(request.POST)
        
        if form.is_valid():
            pass

    context = {
    'title' : 'Profile',
    'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
    'class' : 'fastfood_1',  
    'profile_image' : customer_info.profile_image,
    'gender' : customer_info.gender,
    'form' : form
    }
    return render(request, 'customer/profile.html', context)

@allowed_user
def editProfile(request):

    customer_info = Customer.objects.get(user_id = request.user.id)

    customer_form = CustomerInfoFrom(instance= customer_info)

    user_form = UpdateCustomerForm(instance=request.user)

    user_form.initial["birthdate"] = customer_info.birthdate

    context = {
    'title' : 'Edit Profile',
    'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
    'class' : 'fastfood_1', 
    'profile_image' : customer_form.initial["profile_image"],
    'gender' : customer_form.initial["gender"],
    'last_updated_at' : customer_info.updated_at,
    'user_form' : user_form,
    'customer_form' : customer_form
    }
    return render(request, 'customer/update_profile.html', context)