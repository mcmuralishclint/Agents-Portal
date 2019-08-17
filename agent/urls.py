from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path('user/',include('user.urls')),
    path('accounts/', include('allauth.urls')), #Allauth
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
