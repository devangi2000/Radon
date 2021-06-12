from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides),'product': products}
    # allProds=[[products, range(1, nSlides), nSlides],[products, range(1, nSlides), nSlides]]
    
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        print(prod)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
        print(allProds)
    params = {'allProds': allProds }
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('Contact Page')

def tracker(request):
    return HttpResponse('Tracker Page')

def search(request):
    return HttpResponse('Search Page')

def productView(request):
    return HttpResponse('Product View Page')

def checkout(request):
    return HttpResponse('Checkout Page')
