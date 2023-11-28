from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.db.models.functions import Lower
from django.contrib import messages
from django.db.models import Q # This is for searching queries
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required, user_passes_test
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist


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
    Display the details of a specific product,
    including its reviews and rating form
    """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST" and request.user.is_authenticated:
        has_bought_product = has_bought(request.user, product)
        
        try:
            reviewed = Review.objects.get(user__id=request.user.id, product__id=product_id)
            review_form = ReviewForm(request.POST, instance=reviewed)
            review_form.save()
            messages.success(request, 'Only one review per customer! Your review has been updated!')
            return redirect("product_detail", product_id=product_id)

        except Review.DoesNotExist:
            review_form = ReviewForm(request.POST)

            if review_form.is_valid():
                if has_bought_product:
                    review = review_form.save(commit=False)
                    review.user = request.user
                    review.product = product
                    review.save()
                    messages.success(request, 'Review has been submitted')
                    return redirect("product_detail", product_id=product_id)
                else:
                    messages.error(request, "You can only write a review for products you have bought.")
            else:
                messages.error(request, "Invalid form submission. Please check your inputs.")
    else:
        has_bought_product = has_bought(request.user, product) if request.user.is_authenticated else False
        review_form = ReviewForm(initial={'has_bought': request.user.is_authenticated and has_bought_product})

    reviews = product.review_set.all().order_by("-created_at")
    average_rating = product.average_rating()
    star_percentages = {rating: (average_rating / 5) * 100 for rating in range(1, 6)}
    
    one_star_count = Review.objects.filter(product_id=product_id, rating=1).count()
    two_star_count = Review.objects.filter(product_id=product_id, rating=2).count()
    three_star_count = Review.objects.filter(product_id=product_id, rating=3).count()
    four_star_count = Review.objects.filter(product_id=product_id, rating=4).count()
    five_star_count = Review.objects.filter(product_id=product_id, rating=5).count()

    total_reviews = five_star_count + four_star_count + three_star_count + two_star_count + one_star_count

    if total_reviews > 0:
        five_star_percentage = (five_star_count / total_reviews) * 100
        four_star_percentage = (four_star_count / total_reviews) * 100
        three_star_percentage = (three_star_count / total_reviews) * 100
        two_star_percentage = (two_star_count / total_reviews) * 100
        one_star_percentage = (one_star_count / total_reviews) * 100
    else:
        # Handle the case when there are no reviews to avoid division by zero
        five_star_percentage = 0
        four_star_percentage = 0
        three_star_percentage = 0
        two_star_percentage = 0
        one_star_percentage = 0

    context = {
        "product": product,
        "reviews": reviews,
        "review_form": review_form,
        "average_rating": average_rating,
        "star_percentages": star_percentages,
        "review_count": reviews.count(),
        "has_bought": has_bought_product,  # Update this line
        'on_product_page': True,
        'one_star_count': one_star_count,
        'two_star_count': two_star_count,
        'three_star_count': three_star_count,
        'four_star_count': four_star_count,
        'five_star_count': five_star_count,
        'five_star_percentage': five_star_percentage,
        'four_star_percentage': four_star_percentage,
        'three_star_percentage': three_star_percentage,
        'two_star_percentage': two_star_percentage,
        'one_star_percentage': one_star_percentage,
    }
    return render(request, "products/product_detail.html", context)


def has_bought(user, product):
    """
    Check if the specified user 
    has bought the given product
    """
    # Use filter instead of get to handle MultipleObjectsReturned
    order_line_items = OrderLineItem.objects.filter(order__user_profile__user=user, product=product)
    
    return order_line_items.exists()  # Check if at least one order line item exists


@user_passes_test(lambda u: u.is_superuser, login_url='home')
@login_required
def delete_review(request, review_id):
    """ 
    Delete a review if the user is a superuser
    """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review is deleted!')
    return redirect('product_detail', product_id=review.product.id)


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
    messages.success(request, f"{product.name} has been deleted")
    return redirect(reverse('products'))
