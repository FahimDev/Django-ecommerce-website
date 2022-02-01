from shop.models import BillingAddress, Order, OrderItems,Product,ProductImage,Category, Review
from django.shortcuts import redirect, render
from http.client import HTTPResponse
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from pprint import pp, pprint
from django.core import serializers
from django.http import JsonResponse
import json

from django.db.models import Sum,Value,F

from django.core.serializers.json import DjangoJSONEncoder
from django.db import transaction

from django.forms import model_to_dict


def cartProduct(request): 
    
    products = request.POST.get('data')
   

    if len(products) > 2:
        
        # the result is a Python dictionary:
        products = json.loads(products)

        prod_id = []
        prod_q = []
        for p in products:
            if len(p["id"]) < 1:
                continue
            prod_id.append(int(p["id"]))
            prod_q.append(int(p["quantity"]))  

        item_list = Product.objects.filter(pk__in=prod_id).values()

        cartItem = { }
        cart = []
        for item in list(item_list):
            for p in products:
                if p["id"] == str(item['id']):
                    id = item['id']
                    for index in item.keys():
                        cartItem[index] = item[index]

                    cartItem['quantity'] = p["quantity"]
                    cartItem['image'] = ProductImage.objects.filter(product = Product.objects.get(pk = id)).values_list('product_img_src', flat=True).first()

                    temp = cartItem.copy()
                    cart.append(temp)
                
                cartItem.clear()

        json_items = json.dumps(cart,cls= DjangoJSONEncoder)

        return HttpResponse(json_items, content_type="application/json")
    else:
        print("Data retrive problem!")
        return HttpResponse("Data retrive problem!")

def checkout(request):

    try:
        billing_address = BillingAddress.objects.get(customer = request.user.customer, status = 1)
    except:
        billing_address = None 

    if request.method == 'POST':
        products = request.POST.get('data')
        comment = request.POST.get('comment')

        products = json.loads(products)
        comment = json.loads(comment)

        if request.user.is_anonymous:
            return HttpResponse("401", content_type="application/json")
        else:
            try:
                with transaction.atomic():
                    order = Order()
                    order.comment = comment
                    order.billing_addr = billing_address
                    order.customer = request.user.customer
                    order.save()

                    
                    for p in products:
                        if len(p["id"]) < 1:
                            continue
                        items = OrderItems()
                        prod = Product.objects.get(pk=p["id"])
                        items.order = order
                        items.product = prod
                        items.quantity = p["quantity"]
                        items.save()

                    return HttpResponse("201", content_type="application/json")
            except:
                return HttpResponse("400", content_type="application/json")
   
    context = {
        'meta_title' : 'The New Day a Cloud kitchen of Bangladesh',
        'meta_description' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'title' : 'View Cart',
        'h1_tag' : 'The New Day (TND) is a Cloud Kitchen of Fast Food & Restaurant with Multi Cuisine',
        'class' : 'fastfood_1',
        'billing_address' : billing_address
    }

    return render(request, 'order/checkout.html',context)