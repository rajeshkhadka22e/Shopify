from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.shortcuts import render, get_object_or_404
from.models import Customer,Cart,Product,OrderPlaces

class homeView(View):
    def get(self, request):
        Top_wear = Product.objects.filter(Category='T')
        Bottom_wear = Product.objects.filter(Category='B')
        Laptop = Product.objects.filter(Category='L')
        Mobile = Product.objects.filter(Category='M')

        
        context = {
            'Top_wear': Top_wear,
            'Bottom_wear': Bottom_wear,
            'Laptop': Laptop,
            'Mobile': Mobile,
            
        }
        return render(request, 'app/home.html', context)

class ProductView(View):
    def get(self, request,pk):
        Top_wear = Product.objects.filter(Category='T')
        Bottom_wear = Product.objects.filter(Category='B')
        Laptop = Product.objects.filter(Category='L')
        Mobile = Product.objects.filter(Category='M')

       
        context = {
            'Top_wear': Top_wear,
            'Bottom_wear': Bottom_wear,
            'Laptop': Laptop,
            'Mobile': Mobile,
            'pk':pk,
        }
        return render(request, 'app/product_view.html', context)



class product_detail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)  # Use get_object_or_404 for better error handling
        context = {
            'product': product
        }
        return render(request, 'app/productdetail.html', context)



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
    print(reverse('buy-now'))
    return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
