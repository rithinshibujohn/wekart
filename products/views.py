from django.shortcuts import render, get_object_or_404
from . models import Product
from django.core.paginator import Paginator
from  .forms import ProductSearchForm
from django.db.models import Q 

# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]
    context={   
             'featured_products':featured_products,
             'latest_products':latest_products
    }
    print(context)
    return render(request,'index.html',context)

def list_product(request):
    """_summary_
    return products list page 
    
    Args:
    request(_type_): _description_
    
    Returns:
    _type_: _description_
    """
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('priority')
    product_paginator=Paginator(product_list,4)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products.html',context)

def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render(request,'product_details.html',context)

def search_view(request):
    form = ProductSearchForm(request.GET)
    products = Product.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        products = products.filter(title__icontains=query)

    return render(request, 'search_result.html', {'form': form, 'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    product_title_words = product.title.split()

    # Build the query to prioritize similar products
    similar_products_query = Q()
    for word in product_title_words:  # prioritize first three words
        similar_products_query |= Q(title__icontains=word)

    similar_products = Product.objects.filter(
        similar_products_query & ~Q(pk=pk)
    ).distinct()[:4]  # Limit the number of similar products displayed

    context = {
        'product': product,
        'similar_products': similar_products
    }
    return render(request, 'product_details.html', context)

def terms(request):
    return render(request,'terms.html')