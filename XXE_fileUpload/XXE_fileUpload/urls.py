from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xmlapp/', include('xmlapp.urls')),
    path('', include('xmlapp.urls')),
]
