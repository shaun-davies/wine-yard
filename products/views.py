from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Country

# Create your views here.

def all_products(request):
    """ A view to to show all products """

    products = Product.objects.all()
    query = None
    categories = None
    countries = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'country' in request.GET:
            countries = request.GET['country'].split(',')
            products = products.filter(country__name__in=countries)
            countries = Country.objects.filter(name__in=countries)
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria was entered!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_countries': countries,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to to show single product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)