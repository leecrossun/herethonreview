from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import review.views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', review.views.home, name="home"),
    path('<int:blog_id>/', review.views.detail, name="detail"),
    path('new/', review.views.create, name="new"),
    path('update/<int:pk>', review.views.update, name='update'),
    path('delete/<int:pk>', review.views.delete, name="delete"),
    path('accounts/', include('allauth.urls')),
    path('<int:blog_id>', review.views.detail, name="detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
