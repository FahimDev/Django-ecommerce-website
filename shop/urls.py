from django.urls import path

from shop.views import public
from . import views

urlpatterns = [
    path('', views.public.welcome,name='welcome'),
    path('product-category', views.public.category,name= 'collections'),
    path('products-by-category', views.public.categoryProducts, name='prod_collection'),
    path('product-detail',views.public.details, name= 'prod_details'),
    path('customer-registration', views.public.registration, name= 'cus_reg'),
    path('user-login', views.public.loginPage, name= 'login'),
    path('flush-logout', views.public.logoutUser, name= 'logoutFlush'),
    path('404', views.public.error, name= '404')
]