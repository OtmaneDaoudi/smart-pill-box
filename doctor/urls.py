from django.urls import path
from .views import get_patients, get_alerts

app_name = "doctors"

urlpatterns = [
    path('patients/', get_patients, name="patients"),
    path('alerts/<int:patient_id>', get_alerts, name="alerts")
]