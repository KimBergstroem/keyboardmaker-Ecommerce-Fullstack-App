from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('bag/', include('bag.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
