from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaces

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'user', 'locality', 'city', 'zipcode', 'state')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','Title', 'selling_price', 'Discounted_price', 'Description', 'Brand', 'Category', 'Product_image')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'Product', 'Quantity')

class OrderPlacesAdmin(admin.ModelAdmin):
    list_display = ('id','User', 'Customer', 'Product', 'Quantity', 'ordered_date', 'status')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(OrderPlaces, OrderPlacesAdmin)
