from django.shortcuts import render


def index(request):
    """
    View to return the index page
    """
    return render(request, 'home/index.html')


def contact(request):
    return render(request, 'home/support/contact.html')


def company(request):
    return render(request, 'home/information/company.html')


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
