from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post


def index(request):
    """
    View to return the index page
    """
    posts = Post.objects.all()
    # Fetch the three newest posts for display
    latest_posts = Post.objects.order_by('-created_on')[:3]

    context = {
        'posts': latest_posts,
    }
    return render(request, 'home/index.html', context)


def contact(request):
    return render(request, 'home/support/contact.html')


def company(request):
    return render(request, 'home/information/company.html')


def contact_form(request):
    """
    Contact form view
    """
    template = 'home/support/contact_form.html'
    form = ContactForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ContactForm(request.POST, request.FILES)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.user = request.user
                contact.save()
                messages.success(request, 'Successfully form submission!')
                return redirect(reverse('contact_form'))
            else:
                messages.error(request, 'Failed to submit the form. Please ensure the form is valid.')
        else:
            messages.warning(request, 'You need to be logged in.')

    context = {
        'form': form,
    }
    return render(request, template, context)


def partners(request):
    return render(request, 'home/information/partners.html')


def payments(request):
    return render(request, 'home/information/payments.html')


def privacy_policy(request):
    return render(request, 'home/information/privacy_policy.html')


def return_policy(request):
    return render(request, 'home/information/return_policy.html')


def shipping_policy(request):
    return render(request, 'home/information/shipping_policy.html')


def terms_of_service(request):
    return render(request, 'home/information/terms_of_service.html')


def warranty_policy(request):
    return render(request, 'home/information/warranty_policy.html')
