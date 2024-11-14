from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'adao_app/index.html')


def product_list(request):
    products = Product.objects.all()  
    return render(request, 'adao_app/product_list.html', {'products': products})


def about(request):
    return render(request, 'adao_app/about.html')


def contact(request):
    return render(request, 'adao_app/contact.html')


def login_view(request):
    return render(request, 'adao_app/login.html')


def cart(request):
    return render(request, 'adao_app/cart.html')