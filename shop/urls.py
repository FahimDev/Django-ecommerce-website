from django.conf.urls import handler404
from django.urls import path
from django.contrib import admin

from shop.views import public
from . import views

#handler404 = views.public.error

urlpatterns = [
    path('', views.public.welcome,name='welcome'),
    path('admin/', admin.site.urls, name='admin'),
    path('product-category', views.public.category,name= 'collections'),
    path('products-by-category', views.public.categoryProducts, name='prod_collection'),
    path('product-detail',views.public.details, name= 'prod_details'),
    path('customer-registration', views.public.registration, name= 'cus_reg'),
    path('user-login', views.public.loginPage, name= 'login'),
    path('flush-logout', views.public.logoutUser, name= 'logoutFlush'),
    path('404', views.public.error, name= '404'),

    path('test', views.public.test, name= 'test'),
    #path(r'^admin/(.*)', admin.site.root),

]