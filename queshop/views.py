from django.shortcuts import render
from .models import Products


def index(request):
    products = Products.objects.all().select_related()
    lastest_prod = Products.objects.all().select_related().order_by('-id')[:3]
    data = {
        'products': products,
        'lastest_prod':lastest_prod
    }
    return render(request,'index.html',data)

def blog(request):
    return render(request,'blog.html')

def blog_details(request):
    return render(request,'blog-details.html')

def checkout(request):
    return render(request,'checkout.html')

def shop_details(request,id):
    prod = Products.objects.get(id=id)
    return render(request,'shop-details.html',{'prod':prod})

def contact(request):
    return render(request,'contact.html')