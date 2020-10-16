from django.shortcuts import render
from .models import Product
from math import ceil


# Create your views here.

def index(request):
    allProducts = Product.objects.all()
    n = len(allProducts)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # params = {'no_of_slide': nSlides,
    #           'range': range(1, nSlides),
    #           'product': allProducts,
    #
    #           }

    allProds = [[allProducts,range(1,len(allProducts)),nSlides],
                [allProducts, range(1, len(allProducts)), nSlides]
                ]
    params = {'allProds':allProds}


    return render(request, 'shop/index.html', params)


def programTest(request):

    allProduct = Product.objects.all()
    dictPro = {
        'product':allProduct,
        'range':range(1,6),
        'nSlide':2
    }
    print(dictPro)
    return render(request,'shop/programTest.html',dictPro)



def about(request):
    return render(request, 'shop/about.html')


