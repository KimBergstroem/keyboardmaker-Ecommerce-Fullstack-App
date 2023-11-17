from django.shortcuts import render
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('product'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O6uCHDYbVw9acKAvDoWn8klUVbltUrSdiPkajNwWp132LjTjyP7mcAowdagqKD2bOBYiPoi3vrz7zySq7vhYC2U00cRRM2gbz',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
