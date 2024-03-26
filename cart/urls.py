from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('cart_add/',views.add_cart,name='cart_add'),
    path('shopping-cart/',views.Shopping.as_view(), name='shop_cart'),
    path('cart_delete/', views.delete_cart, name='cart_delete'),
    path('save_shopping/',views.save_shopping,name='save_shopping')
]