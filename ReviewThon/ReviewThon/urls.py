from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import review.views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', review.views.home, name="home"),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
