from django.contrib import admin
from django.urls import path, include
from .views import login_view

app_name = "authentication"

urlpatterns = [
    path('login/', login_view, name="login")
]