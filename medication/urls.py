from django.urls import path
from .views import get_medications, add_new, get_prescription, update_prescription, delete_prescription, daily_intake, delete_medication

app_name = "medications"

urlpatterns = [
    path('meds/', get_medications, name="meds"),
    path('add_new/', add_new, name="add_new"),
    path('prescription/<int:patient_id>', get_prescription, name="prescription"),
    path("prescription/update", update_prescription, name="update_prescription"),
    path("prescription/delete", delete_prescription, name="delete_prescription"),
    path("prescription/daily_intake", daily_intake, name="daily_intake"),
    path("medication/delete/<int:medication_id>", delete_medication, name="delete_medication")
]