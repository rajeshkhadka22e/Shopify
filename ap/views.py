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



def mobile(request, data=None):
    if data is None:
        # Show all mobile products if no filter is provided
        mobiles = Product.objects.filter(Category='M')
    elif data in ['Redmi', 'Samsung']:
        # Filter by brand (Change from 'brand' to 'Brand' to match your model)
        mobiles = Product.objects.filter(Category='M', Brand=data)  # Changed 'brand' to 'Brand'
    elif data == 'Below':
        # Filter for discounted prices below 10,000
        mobiles = Product.objects.filter(Category='M', Discounted_price__lt=10000)
    elif data == 'Above':
        # Filter for discounted prices above 10,000
        mobiles = Product.objects.filter(Category='M', Discounted_price__gt=10000)
    else:
        # Handle case where the data does not match any known filters
        mobiles = []  # Default to an empty list if no match is found

    return render(request, 'app/mobile.html', {'mobiles': mobiles})  # Pass filtered products to the template

def laptop(request, data=None):
    if data is None:
        # Show all mobile products if no filter is provided
        laptop = Product.objects.filter(Category='L')
    elif data in ['MAC', 'Samsung']:
        # Filter by brand (Change from 'brand' to 'Brand' to match your model)
        laptop = Product.objects.filter(Category='L', Brand=data)  # Changed 'brand' to 'Brand'
    elif data == 'Below':
        # Filter for discounted prices below 10,000
        laptop = Product.objects.filter(Category='L', Discounted_price__lt=50000)
    elif data == 'Above':
        # Filter for discounted prices above 10,000
        laptop = Product.objects.filter(Category='L', Discounted_price__gt=100000)
    else:
        # Handle case where the data does not match any known filters
        laptop = []  # Default to an empty list if no match is found

    return render(request, 'app/laptop.html', {'laptop': laptop})  # Pass filtered products to the template

def topwears(request, data=None):
    if data is None:
        # Show all mobile products if no filter is provided
        topwears = Product.objects.filter(Category='T')
    elif data in ['tshirt', 'vest']:
        # Filter by brand (Change from 'brand' to 'Brand' to match your model)
        mobitopwearsles = Product.objects.filter(Category='T', Brand=data)  # Changed 'brand' to 'Brand'
    elif data == 'Below':
        # Filter for discounted prices below 10,000
        topwears = Product.objects.filter(Category='T', Discounted_price__lt=10000)
    elif data == 'Above':
        # Filter for discounted prices above 10,000
        topwears = Product.objects.filter(Category='T', Discounted_price__gt=10000)
    else:
        # Handle case where the data does not match any known filters
        topwears = []  # Default to an empty list if no match is found

    return render(request, 'app/topwears.html', {'topwears': topwears})  # Pass filtered products to the template

def bottomwears(request, data=None):
    if data is None:
        # Show all mobile products if no filter is provided
        bottomwears = Product.objects.filter(Category='B')
    elif data in ['pant', 'halfpant']:
        # Filter by brand (Change from 'brand' to 'Brand' to match your model)
        bottomwears = Product.objects.filter(Category='B', Brand=data)  # Changed 'brand' to 'Brand'
    elif data == 'Below':
        # Filter for discounted prices below 10,000
        bottomwears = Product.objects.filter(Category='B', Discounted_price__lt=50000)
    elif data == 'Above':
        # Filter for discounted prices above 10,000
        bottomwears = Product.objects.filter(Category='B', Discounted_price__gt=100000)
    else:
        # Handle case where the data does not match any known filters
        bottomwears = []  # Default to an empty list if no match is found

    return render(request, 'app/bottomwears.html', {'bottomwears': bottomwears})  # Pass filtered products to the template

def login(request):
 return render(request, 'app/login.html',)

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
