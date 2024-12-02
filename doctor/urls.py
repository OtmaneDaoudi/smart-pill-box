from django.urls import path
from .views import get_patients

app_name = "doctors"

urlpatterns = [
    path('patients/', get_patients, name="patients")
]