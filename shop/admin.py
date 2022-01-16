from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Category
# Register your models here.


class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Category, MyModelAdmin)