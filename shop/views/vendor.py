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
from shop.forms import CreateCategoryForm

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
            #instance = form.instance
            #instance.customer = request.user.customer
                
            #instance.banner_img_path = form.cleaned_data.get('imageblob_banner')
            print('Flag1')
            form.save()
            print(form.errors)
            messages.success(request, 'New Category Created')
            return redirect('add_category')
            """
            try:

            except:
                messages.info(request, form.errors)
                return redirect('welcome')
            """

    return render(request, 'vendor/add_category.html', context)