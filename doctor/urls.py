from django.contrib import admin
from django.urls import path, include
from .views import get_patients

urlpatterns = [
    path('patients/', get_patients)
]
