from django.shortcuts import render, redirect


def view_bag(request):
    """
    A View that renders the bag contents page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {}) # create or update the bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity # if the item already in bag, increase the quantity
    else:
        bag[item_id] = quantity # else add the item to the bag
    
    request.session['bag'] = bag
    return redirect(redirect_url)
