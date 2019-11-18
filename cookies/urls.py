from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('baker', views.baker, name='baker'),
]