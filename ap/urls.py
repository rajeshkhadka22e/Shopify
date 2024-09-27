from django.urls import path
from .views import (
    homeView, product_detail, add_to_cart, buy_now, 
    profile, address, orders, change_password, 
    mobile, laptop, topwears, bottomwears, login, 
    customerregistration, checkout
)

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('product/<int:pk>/', product_detail.as_view(), name='product-detail'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('buy-now/', buy_now, name='buy-now'),
    path('profile/', profile, name='profile'),
    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),
    path('change-password/', change_password, name='changepassword'),
    path('mobile/', mobile, name='mobile'),  # Route for showing all mobiles
    path('mobile/<slug:data>/', mobile, name='mobiledata'),  # Route for filtering mobiles
    path('laptop/', laptop, name='laptop'),  # Route for showing all laptops
    path('laptop/<slug:data>/', laptop, name='laptopdata'),
    path('topwears/', topwears, name='topwears'),
    path('topwears/<slug:data>/', topwears, name='topwearsdata'),
  # Route for showing all topwears
    path('bottomwears/', bottomwears, name='bottomwears'),  # Route for showing all bottomwears
    path('bottomwears/<slug:data>/', bottomwears, name='bottomwearsdata'),
    path('login/', login, name='login'),
    path('customer-registration/', customerregistration, name='customerregistration'),
    path('checkout/', checkout, name='checkout'),
]
