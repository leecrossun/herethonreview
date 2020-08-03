from django.contrib import admin
from django.urls import path
import review.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', review.views.home, name="home"),
]
