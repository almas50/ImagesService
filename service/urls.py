from django.contrib import admin
from django.urls import path, include
from .views import ImageCreateView, ImageView

urlpatterns = [
    path('', ImageCreateView.as_view(), name='home'),
    path('all/', ImageView.as_view(), name='images')
]
