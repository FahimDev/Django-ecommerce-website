from django.contrib.auth import authenticate,login, logout
from shop.decorator import auth_user_page_restriction,allowed_user #Custom DesignPattern

from django.urls.conf import path
from django.contrib.auth.models import Group
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponseRedirect

from shop.forms import BillingAddressForm,UpdateCustomerForm,CustomerInfoFrom
from django.contrib import messages

from django.contrib.auth.models import User
from django.db import transaction
from shop.models import BillingAddress, Customer


@allowed_user
def profile(request):
    

    try:
        customer_info = Customer.objects.get(user_id = request.user.id)

        form = BillingAddressForm(initial={'customer': request.user.customer.id})

        address = BillingAddress.objects.filter(customer_id = request.user.customer.id)
    except:
        messages.info(request, 'Something went wrong! Data Retriving Error')
        return render(request, 'customer/profile.html')
    
    print(request.user.customer.id)

    if request.method == 'POST':
        form = BillingAddressForm(request.POST)
        
        if form.is_valid():
            pass

    context = {
    'title' : 'Profile',
    'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
    'class' : 'fastfood_1',  
    'customer_info' : customer_info,
    'gender' : customer_info.gender,
    'address' : address,
    'form' : form
    }
    return render(request, 'customer/profile.html', context)

@allowed_user
def editProfile(request):

    customer_info = Customer.objects.get(user_id = request.user.id)

    customer_form = CustomerInfoFrom(instance= customer_info)

    user_form = UpdateCustomerForm(instance=request.user)


    if request.method == 'POST':
        
        user_info = User.objects.get(id = request.user.id)
        user_form = UpdateCustomerForm(request.POST,instance = user_info)
        customer_form = CustomerInfoFrom(request.POST,request.FILES,instance = customer_info)
        
        print(customer_form.errors)#{{customer_form.initial.profile_image}}

        if user_form.is_valid() and customer_form.is_valid():
            try:
                user_form.save()
                customer_form.save()
                #Customer.objects.filter(user = request.user.id).update(user_form)
                messages.success(request, 'Profile Updated')
                return redirect('cus_profile')
            except:
                messages.info(request, 'Something went wrong!')
                return redirect('cus_profile')       

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


@allowed_user
def addBillingAddress(request):
    if request.method == 'POST':
        address_form = BillingAddressForm(request.POST)
        #address_form.initial['user'] = request.user.id
        
        print(address_form.errors)
        if address_form.is_valid():

            try:
                instance = address_form.instance
                instance.customer = request.user.customer
                instance.save()
                messages.success(request, 'New Billing Address Created')
                return redirect('cus_profile')
            except:
                messages.info(request, 'Something went wrong! Please Try again')
                return redirect('cus_profile')

def setBillingAddress(request, sent_pk):
    try:
        with transaction.atomic():
            BillingAddress.objects.filter(customer_id = request.user.customer.id).update(status = 0)
            BillingAddress.objects.filter(pk = sent_pk, customer_id = request.user.customer.id).update(status = 1)
            messages.success(request, 'Billing Address Selected')
            return redirect('cus_profile')
    except:
        messages.info(request, 'Something went wrong! Please try again.')
        return redirect('cus_profile')
            
@allowed_user
def deleteBillingAddress(request, sent_pk):
    try:
        address = BillingAddress(pk = sent_pk, customer_id = request.user.customer.id)
        address.delete()
        messages.success(request, 'Billing Address Removed')
        return redirect('cus_profile')
    except:
        messages.info(request, 'Something went wrong!')
        return redirect('cus_profile')


