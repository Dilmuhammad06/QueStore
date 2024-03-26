from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('blog-details/',views.blog_details, name='blog_details'),
    path('blog/',views.blog, name='blog'),
    path('checkout/',views.checkout, name='checkout'),
    path('contact/',views.contact, name='contact'),
    path('shop-details/<int:id>/',views.shop_details, name='shop_details')
]