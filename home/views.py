from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import ContactForm, NewsletterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from blog.models import Post
from .models import SubscribedUsers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.mail import EmailMessage


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


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must type legit email address to subscribe to a Newsletter")
            return redirect("/")

        if User.objects.filter(email=email).exists():
            messages.error(request, f"A user with the email {email} already exists. Please log in to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))


@user_passes_test(lambda user: user.is_superuser)
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, f"EasyKeyboardMaker <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='home/newsletter.html', context={'form': form})
