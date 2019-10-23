from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cookies/', include('cookies.urls')),
    path('admin/', admin.site.urls),
]
