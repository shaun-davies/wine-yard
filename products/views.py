from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Country, ProductReview
from .forms import ProductForm, ReviewForm

# Products

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
    """ A view to to show single product details and reviews"""

    product = get_object_or_404(Product, pk=product_id)

    reviews = ProductReview.objects.filter(product=product)

    context = {
        'product': product,
        'reviews': reviews,
    }
    
    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Ensure form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted.')
    return redirect(reverse('products'))

# Reviews

def add_review(request, product_id):
    """ Add a review to a product """

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=product)
        if form.is_valid():
            ProductReview.objects.create(
                product=product,
                user=request.user,
                review=request.POST.get('review'),
                user_name=request.POST.get('user_name'),
                rating=int(request.POST.get('rating'))
            )
            messages.success(request, f'Successfully added review of {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to review product. Ensure form is valid.')
    else: 
        form = ReviewForm(instance=product)
    
    template = "products/add_review.html"
    context = {
        'form': form,
        'product': product,
        'user': request.user,
    }
    return render(request, template, context)
