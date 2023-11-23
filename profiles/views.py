from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm, UpdatePersonalInfoForm
from django.contrib import messages
from checkout.models import Order
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@login_required
def profile(request):
    """
    Display the user's profile with
    order history and defualt shipping form
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template ='profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True # For making the success message only display the message and not the shopping bag
        # set this boolean to true and then in the code, AND NOT
    }
    return render(request, template, context)


@login_required
def profile_update(request):
    """
    View for updating the user's personal information
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    form = UserProfileForm(request.POST, instance=profile)
    if request.method == 'POST':
        personal_form = UpdatePersonalInfoForm(request.POST, instance=profile)
        if personal_form.is_valid():
            personal_form.save()
            messages.success(request, 'Personal information updated successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        personal_form = UpdatePersonalInfoForm(instance=profile)

    context = {
        'personal_form': personal_form,
        'orders': orders,
        'form': form,
    }
    return render(request, 'profiles/profile_update.html', context)


@login_required
def profile_delete(request, pk):
    """
    Handles the deletion of a user profile and related objects
    """
    user = get_object_or_404(User, id=pk)
    logout(request)
    user.delete() 
    messages.warning(request, "Your account has been deleted")  
    # Redirect to the home page
    return redirect("home")


def order_history(request, order_number):
    """
    Display users order history
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)


def profile_agreement(request):
    """
    Render the profil_agreement.html template
    """
    return render(request, "profiles/profile_agreement.html")
