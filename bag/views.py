from django.shortcuts import render

def view_bag(request):
    """
    A View that renders the bag contents page
    """
    return render(request, 'bag/bag.html')

