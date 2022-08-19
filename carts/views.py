from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Cart,Cartitem
from store.models import Product

# Create your views here.

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
     #cart model
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    #cartitem model
    try:
        cart_item=Cartitem.objects.get(product=product, cart=cart)
        cart_item.quantity=cart_item.quantity +1
        #cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item=Cartitem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
        )
        cart_item.save()
        return redirect('/cart')
        return HttpResponse(cart_item.product)
def cart1(request,total=0,quantity=0,cart_item=None):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    cart_item=Cartitem.objects.filter(cart=cart,is_available=True)
    for ci in cart_item:
        total=total+ci.product.price*ci.quantity
    tax=(5*total)/100
    grand_total=tax+total
    return render(request,'cart.html',{'cart_item':cart_item,'total':total,'tax':tax,'gtotal':grand_total})   