'''
In object-oriented programming, the decorator pattern is a design pattern.
Decorator is a structural design pattern that lets you attach new behaviors to 
objects by placing these objects inside special wrapper objects that contain the behaviors.
In simple language Decorator is a FUNCTION which takes another FUNCTION as a parameter 
'''
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest, request
from django.shortcuts import redirect,render
from django.urls.base import reverse

#The *args keyword sends a list of values to a function

#The *kwargs sends a dictionary with values associated with keywords to a function.

def auth_user_page_restriction(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {
                'title' : '404',
                'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
                'class' : 'fastfood_1',  

                'caption': 'You are already logged in!!!',
                'sub_text': 'Looks like the page you are trying to visit does not exist for this session. Please check the URL and try your lick again'
            }

            return render(request, 'visitors/404.html', context)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_user(view_func_allow):
    def wrapper_func_allow(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Customer':
            return view_func_allow(request, *args, **kwargs)
        
        else:
            return redirect('admin:index')
    return wrapper_func_allow


def allowed_users(allowed_roles = []):
    def decorator(view_func_list):
        def wrapper_func_list(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func_list(request, *args, **kwargs)
            else:
                return HttpResponse("You are not Authorized!")
        return wrapper_func_list
    return decorator
