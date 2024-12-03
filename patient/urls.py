from django.urls import path
from .views import get_prescriptions

app_name = "patients"

urlpatterns = [
    path("todo/", get_prescriptions, name="todo")
]