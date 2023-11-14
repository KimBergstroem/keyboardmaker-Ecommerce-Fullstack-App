from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q # This is for searching queries
from .models import Product, Category


def all_products(request):
    """
    A view to show all products, including sorting
    and search queries
    """
    products = Product.objects.all()
    query = None  # Initialize the 'query' variable to None
    categories = None

    if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                products = products.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)

    if request.GET:  # Check if there are any GET parameters in the request
        if 'q' in request.GET:  # Check if the 'q' parameter exists in the GET parameters
            query = request.GET['q']  # Retrieve the value of the 'q' parameter from the GET request

            if not query:  # Check if the 'q' parameter is empty (no search criteria provided)
                # If 'q' is empty, show an error message using the Django messages framework
                messages.error(request, "You didn't enter any search criteria!")

                # Redirect the user to a page named 'products' (likely a search results page)
                return redirect(reverse('products'))

    # Create a query for searching products based on name and description
    # The | (OR) operator combines two conditions: name_icontains and description_icontains
    queries = Q(name__icontains=query) | Q(description__icontains=query)

    # Assuming 'products' is a queryset (e.g., a list of products), filter the products based on the queries
    products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show specific product detail page
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
