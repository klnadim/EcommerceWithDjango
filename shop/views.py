from django.shortcuts import render
from .models import Product
from math import ceil


# Create your views here.

def index(request):
    # allProducts = Product.objects.all()
    # n = len(allProducts)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # params = {'no_of_slide': nSlides,
    #           'range': range(1, nSlides),
    #           'product': allProducts,
    #
    #           }

    allProds = []
    catProds = Product.objects.values('category','id')

    cats = {item['category'] for item in catProds}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides),nSlides])



    # allProds = [[allProducts,range(1,len(allProducts)),nSlides],
    #             [allProducts, range(1, len(allProducts)), nSlides]
    #             ]


    params = {'allProds':allProds}


    return render(request, 'shop/index.html', params)


def programTest(request):

    allProduct = Product.objects.all()
    dictPro = {
        'product':allProduct,
        'range':range(1,6),
        'nSlide':2
    }

    return render(request,'shop/programTest.html',dictPro)



def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request):
    return render(request, 'shop/productView.html')

def checkout(request):
    return render(request, 'shop/checkout.html')
