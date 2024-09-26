from django.urls import path
from .views import (
    homeView, product_detail, add_to_cart, buy_now, 
    profile, address, orders, change_password, mobile, 
    login, customerregistration, checkout
)

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('product/<int:pk>/', product_detail.as_view(), name='product-detail'),  # Use this as the single entry
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('buy-now/', buy_now, name='buy-now'),
    path('profile/', profile, name='profile'),
    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),
    path('change-password/', change_password, name='changepassword'),
    path('mobile/', mobile, name='mobile'),
    path('login/', login, name='login'),
    path('customer-registration/', customerregistration, name='customerregistration'),
    path('checkout/', checkout, name='checkout'),
]
