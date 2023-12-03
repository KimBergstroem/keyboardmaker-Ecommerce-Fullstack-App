from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('company/', views.company, name='company'),
    path('partners/', views.partners, name='partners'),
    path('payments/', views.payments, name='payments'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('refund-policy/', views.refund_policy, name='refund_policy'),
    path('shipping-policy/', views.shipping_policy, name='shipping_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
]
