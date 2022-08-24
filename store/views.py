from django.shortcuts import render,get_object_or_404,redirect
from store.models import Product
from category.models import category
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.
def store(request,category_slug=None):
    if(category_slug !=None):
        categories=get_object_or_404(category,slug=category_slug)
        products=Product.objects.filter(category=categories,is_available=True)
        paginator =Paginator(products, 1)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count=products.count()
    else:
        products=Product.objects.all().filter(is_available=True)
        paginator =Paginator(products, 1)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count=products.count()
    return render (request,'store.html',{'products':paged_product,'pcount':product_count})

def product_detail(request,category_slug,product_slug):
    single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    return render(request,'product_details.html',{'sproduct':single_product})

def Search(request):
    if request.method=='GET':
        vkeyword=request.GET.get('keyword')
        if vkeyword:
            ganavi=Product.objects.order_by('-created_data').filter(Q(description__icontains=vkeyword) | Q(product_name__icontains=vkeyword)) 
        else:
            return redirect('store')
    return render(request,'store.html',{'products':ganavi})
   # return HttpResponse(vkeyword)