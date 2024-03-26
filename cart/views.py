import uuid

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import View

from users.models import User
from .cart import Cart
from queshop.models import Products, Order, OrderItem


def add_cart(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = request.POST.get('product_id')
        product_num = request.POST.get('product_num')
        product = get_object_or_404(Products, id=product_id)
        cart.add_cart(product,product_num)
        return JsonResponse({'Product':product.name,'Quantity':product_num})

def delete_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        print(product_id)
        cart.delete(product_id)
        return JsonResponse({'Product_id':product_id})


class Shopping(View):
    def get(self,request):
        session = request.session
        cart = session.get('cart', {})
        return render(request, 'shopping-cart.html', {'cart': cart})


def save_shopping(request):
    total = request.POST.get('total')
    user = User.objects.get(id=request.user.id)
    user.balance = request.user.balance - int(total)
    user.save()
    cart = Cart(request)

    order = Order.objects.create(
        user = request.user,
        order_id = uuid.uuid4(),
        total_price = total,
    )
    order.save()
    for info in cart.all_info():
        order_item = OrderItem.objects.create(
            order=order,
            product_id=int(info['id']),
            name=info['name'],
            price=int(info['price']),
            quantity=int(info['quantity'])
        )
        order_item.save()
    cart.clean_cart()
    return redirect('index')