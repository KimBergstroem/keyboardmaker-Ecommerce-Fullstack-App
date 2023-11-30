from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog'),
    path("post_detail/<slug:slug>/", views.PostDetail.as_view(), name="post_detail",),
]