from django.urls import path
from . import views

urlpatterns = [
    path('', views.public.welcome,name='welcome'),
    path('product-category', views.public.category,name= 'collections'),
    path('products-by-category', views.public.categoryProducts, name='prod_collection')
]