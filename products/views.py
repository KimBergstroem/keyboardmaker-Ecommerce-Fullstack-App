from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.db.models.functions import Lower
from django.contrib import messages
from django.db.models import Q # This is for searching queries
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def all_products(request):
    """
    A view to show all products, including sorting
    and search queries
    """
    products = Product.objects.all()
    query = None  
    categories = None
    sort = None
    direction = None


    if request.GET: 
        # Check if sorting and filtering parameters are present in the GET request
        if 'sort' in request.GET:
            # Retrieve the sorting criteria from the 'sort' parameter
            sortkey = request.GET['sort']
            sort = sortkey  # (Optional) Assign the 'sort' variable

            # Check if the sorting criteria is 'name'
            if sortkey == 'name':
                # Change the sorting key to 'lower_name' for case-insensitive sorting
                sortkey = 'lower_name'

                # Annotate the products queryset with a lowercase version of the 'name' field
                # This allows for case-insensitive sorting
                products = products.annotate(lower_name=Lower('name'))
                
            if sortkey == 'category':
                sortkey = 'category__name'

            # Check if the sorting direction is specified
            if 'direction' in request.GET:
                # Retrieve the sorting direction from the 'direction' parameter
                direction = request.GET['direction']

                # Check if the sorting direction is 'desc' (descending)
                if direction == 'desc':
                    # Prepend '-' to the sorting key to indicate descending order
                    sortkey = f'-{sortkey}'

            # Sort the products queryset based on the chosen sorting criteria
            products = products.order_by(sortkey)


        # Search and display specific category in product
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        #Searchbar function in products
        if 'q' in request.GET:  # Check if the 'q' parameter exists in the GET parameters
            query = request.GET['q']  # Retrieve the value of the 'q' parameter from the GET request

            if not query:
                messages.error(request, "You didn't enter any search criteria!")

                # Redirect the user to a page named 'products' (likely a search results page)
                return redirect(reverse('products'))

            # Create a query for searching products based on name and description
            # The | (OR) operator combines two conditions: name_icontains and description_icontains
            queries = Q(name__icontains=query) | Q(description__icontains=query)

            # Assuming 'products' is a queryset (e.g., a list of products), filter the products based on the queries
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = { # Most have context, for passing all the sorting, search function to render the page
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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


@login_required
def add_product(request):
    """ 
    Add a product to the store 
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ 
    Edit a product to the store 
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid')
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
    """ 
    Delete a product to the store 
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
