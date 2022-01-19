from django.conf.urls import handler404
from django.urls import path
from django.contrib import admin

from shop.views import public
from . import views

#handler404 = views.public.error

urlpatterns = [
    path('', views.public.welcome,name='welcome'),
    path('product-category', views.public.category,name= 'collections'),
    path('products-by-category/<slug:sent_slug>/<str:sent_pk>/', views.public.categoryProducts, name='prod_collection'),
    path('product-detail/<slug:sent_slug>/<str:sent_pk>/',views.public.details, name= 'prod_details'),
    path('customer-registration', views.public.registration, name= 'cus_reg'),
    path('user-login', views.public.loginPage, name= 'login'),
    path('flush-logout', views.public.logoutUser, name= 'logout_flush'),
    path('404', views.public.error, name= '404'),

    path('test', views.public.unlock, name= 'unlock'),


    #-------------------->customer
    path('profile', views.customer.profile, name= 'cus_profile'),
    path('update-customer-profile', views.customer.editProfile, name= 'update_customer'),
    path('add-billing-address', views.customer.addBillingAddress, name= 'create_address'),
    path('set-billing-address/<str:sent_pk>/', views.customer.setBillingAddress, name= 'set_address'),
    path('flush-billing-address/<str:sent_pk>/', views.customer.deleteBillingAddress, name= 'flush_address'),

    #-------------------->Vendor
    path('vendor-office', views.vendor.dashboard, name= 'dash'),
    path('add-category', views.vendor.createCategory, name= 'add_category'),

    path('add-product', views.vendor.createProduct, name= 'add_product'),
    path('add-product-photos', views.vendor.addProductPhotos, name= 'add_prod_photo'),

]