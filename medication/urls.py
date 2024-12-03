from django.urls import path
from .views import get_medications, add_new, get_prescription, update_prescription

app_name = "medications"

urlpatterns = [
    path('meds/', get_medications, name="meds"),
    path('add_new/', add_new, name="add_new"),
    path('prescription/<int:patient_id>', get_prescription, name="prescription"),
    path("prescription/update", update_prescription, name="update_prescription")
]