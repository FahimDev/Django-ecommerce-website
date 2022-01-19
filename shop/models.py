from distutils.command.upload import upload
import imp
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT

from django.contrib.auth.models import User
import datetime

from pprint import pprint

#-----------------------------------------------------------------------------------------------------------------
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format('customer/', str(instance.user.username)+'_'+ str(datetime.datetime.now())+str(instance.user.id)+'786'+'.jpg')
    #https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.FileField.upload_to
class Customer(models.Model):
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_BRONGE = 'B'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_GOLD, 'Gold Badge'),
        (MEMBERSHIP_SILVER, 'Silver Badge'),
        (MEMBERSHIP_BRONGE, 'Bronge Badge')
    ]

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_NONE = 'N'

    GENDER_VALUES = [
        (GENDER_MALE,'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_NONE, 'None')
    ]

    profile_image = models.ImageField(null= True, blank= True, upload_to = user_directory_path)
    gender = models.CharField(max_length= 50, choices= GENDER_VALUES, default= GENDER_NONE)
    user = models.OneToOneField(User, null= True, on_delete= models.CASCADE)
    contact = models.CharField (max_length= 15,unique=True)
    social_media_link = models.CharField (max_length= 200)
    birthdate = models.DateTimeField(auto_now=False)
    membership = models.CharField(max_length= 12, choices=MEMBERSHIP_CHOICES, default= MEMBERSHIP_BRONGE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#-----------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------
# def shop_directory_path(instance,filename):

#     #pprint(dir(instance))
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'shop_{0}/{1}'.format('category/', 'category_type_image_'+ str(datetime.datetime.now())+'.jpg')
#     #https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.FileField.upload_to


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    banner_img_path = models.ImageField(max_length=500, null= True, blank= True)
    category_img_path = models.ImageField(max_length=500,null= True, blank= True)
    policy = models.TextField(null= True)
    meta_keywords = models.CharField(max_length=400, null= True)
    meta_description = models.TextField(null= True)
    slug = models.SlugField(unique= True,max_length=150)
    large = models.DecimalField(max_digits=6,decimal_places=2)
    medium = models.DecimalField(max_digits=6,decimal_places=2)
    small = models.DecimalField(max_digits=6,decimal_places=2)
    unit = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'{0}'.format(self.category_name)
#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
class Product(models.Model):

    PACKING_BOTTLE = 'A'
    PACKING_PLASTIC_BOX = 'B'
    PACKING_FOIL_BOX = 'C'
    PACKING_CART_BOX = 'D'
    PACKING_POLY_BAG = 'E' 

    PACKING_TYPES = [
        (PACKING_BOTTLE, 'Bottle'),
        (PACKING_PLASTIC_BOX, 'Plastic Box'),
        (PACKING_FOIL_BOX, 'Foil Sealed Box'),
        (PACKING_CART_BOX, 'Cart Box'),
        (PACKING_POLY_BAG, 'Poly Bag') 
    ]

    PRODUCT_OUT = 'O'
    PRODUCT_STOCKED = 'S'
    PRODUCT_LOW = 'L'
    PRODUCT_BANNED = 'B'

    PRODUCT_STATUS = [
        (PRODUCT_OUT,'out_of_stock'),
        (PRODUCT_STOCKED,'in_stock'),
        (PRODUCT_LOW, 'running_low'),
        (PRODUCT_BANNED, 'banned')
    ]

    product_title = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=400, null= True)
    meta_description = models.TextField(null= True)
    category = models.ForeignKey(Category, related_name='products', on_delete= models.CASCADE)
    merchant = models.PositiveBigIntegerField(default=1) #For Future Development
    video_url = models.URLField(max_length=300)
    slug = models.SlugField()
    product_description = models.TextField()
    product_material = models.TextField()
    product_brand = models.CharField(max_length= 100) 
    packing_type = models.CharField(max_length=100, choices= PACKING_TYPES, default= PACKING_POLY_BAG)
    product_sale = models.DecimalField(max_digits=6,decimal_places=2)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    status = models.CharField(max_length=100,choices= PRODUCT_STATUS, default= PRODUCT_STOCKED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return u'{0}'.format(self.product_title)
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_img_src = models.ImageField(max_length=500, null= True, blank= True)
    img_title = models.CharField(max_length=100, null=  True)
    img_alt = models.CharField(max_length= 400, null= True)
#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------

class BillingAddress(models.Model):
    CURRENT_DELIVERY = 1
    OPTIONAL_ADDRESS = 0
    ORDER_STATUS = [
        (OPTIONAL_ADDRESS, 'Optional Address'),
        (CURRENT_DELIVERY, 'Current Delivery')
    ]

    customer = models.ForeignKey(Customer, null= True, on_delete= models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length= 100)
    zip_code = models.IntegerField()
    division = models.CharField(max_length= 100)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    status = models.CharField(max_length= 100, choices= ORDER_STATUS, default= OPTIONAL_ADDRESS)

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------

class Order(models.Model):

    ORDER_PENDING = 0
    ORDER_ON_PROGRESS = 1
    ORDER_ON_THE_WAY = 2
    ORDER_DELIVERED = 3
    ORDER_CANCEL = 4
    ORDER_FAILED = 5

    ORDER_STATUS = [
        (ORDER_PENDING, 'Pending'),
        (ORDER_ON_PROGRESS, 'On Progres'),
        (ORDER_ON_THE_WAY, 'On The Way'),
        (ORDER_DELIVERED, 'Delivered'),
        (ORDER_CANCEL, 'Cancel'),
        (ORDER_FAILED, 'Failed')
    ]

    customer_id = models.ForeignKey(Customer, on_delete= models.PROTECT)
    #discount_id = 
    billing_addr_id = models.ForeignKey(BillingAddress, on_delete=  models.PROTECT)
    comment = models.TextField(null= True) 
    status = models.CharField(max_length= 100, choices= ORDER_STATUS, default= ORDER_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
class OrderItems(models.Model):
    order_id = models.ForeignKey(Customer, on_delete= models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete= models.SET_NULL, null= True)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    review_title = models.CharField(max_length= 100, default= 'Product Review')
    review_body = models.TextField()
    rating = models.SmallIntegerField()
    verification = models.BooleanField(default= False)
    #if reviewer is email verified status will be True | Registered Customer status will be auto True after login.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
class Advertise(models.Model):

    SIGNUP_SHOW = True
    SIGNUP_HIDE = False

    SIGNUP_STATUS = [
        (SIGNUP_SHOW, 'Show Sign up'),
        (SIGNUP_HIDE, 'Hide Sign up')
    ]

    title = models.CharField(max_length= 50, default= 'NEW SLETTER!')
    subtitle = models.CharField(max_length= 50, default= 'UP TO 70% OFF')
    caption = models.CharField(max_length= 10,default='FOOD')
    signup_visibility = models.CharField(max_length= 50, choices= SIGNUP_STATUS, default= SIGNUP_SHOW)
    advertise_visibility = models.BooleanField(default= False)
#-----------------------------------------------------------------------------------------------------------------