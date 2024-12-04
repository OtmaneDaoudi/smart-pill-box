from django.shortcuts import render, HttpResponse, redirect
from authentication.models import RoleBasedUser
from medication.models import Intake
from authentication.utils import protect_route, UserType
from authentication.models import RoleBasedUser
import json


def serialize_user(user: RoleBasedUser) -> dict:
    if not user: return {}
    return [
        user.user.rolebaseduser.id,
        user.user.first_name,
        user.user.last_name,
        user.user.email
    ]

def serilaize_intake(intake: Intake):
    if not intake: return []

    periods = {
        "M": "Morning",
        "E": "Evening",
        "A": "Afternoon"
    }
    return [
        intake.id,
        intake.prescription.medication.name,
        periods[intake.prescription.period],
        periods[intake.period]
    ]

# Create your views here.
def get_patients(request):
    # redirect if not logged in as a doctor
    response = protect_route(request, UserType.DOCTOR)
    if response: return response
    patients = RoleBasedUser.objects.filter(isDoctor = False)
    table_data = json.dumps([serialize_user(patient) for patient in patients])
    return render(request, "patients.html", {"table_data": table_data, "active": "patients"})

def get_alerts(request, patient_id):
    reponse = protect_route(request, UserType.DOCTOR)
    if reponse: return reponse

    patient = RoleBasedUser.objects.get(id=patient_id)
    prescriptions = patient.target.all()
    faulty_intakes = json.dumps([serilaize_intake(intake) for prescription in prescriptions for intake in prescription.intake_set.all() if intake.period != intake.prescription.period])
    return render(request, "alerts.html", {"table_data": faulty_intakes, "active": "alerts"})