from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog'),
    path("post_create/", views.PostCreateView.as_view(), name="post_create"),
    path("post_detail/<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("post_edit/<slug:slug>", views.PostEditView.as_view(), name="post_edit"),
    path("post_delete/<slug:slug>/delete", views.PostDeleteView.as_view(), name="post_delete"),
]