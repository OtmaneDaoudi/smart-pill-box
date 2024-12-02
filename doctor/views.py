from django.shortcuts import render, HttpResponse, redirect
from authentication.models import RoleBasedUser
from authentication.utils import protect_route, UserType
import json


def serialize_user(user: RoleBasedUser) -> dict:
    if not user: return {}
    return [
        user.user.id,
        user.user.first_name,
        user.user.last_name,
        user.user.email
    ]

# Create your views here.
def get_patients(request):
    # redirect if not logged in as a doctor
    response = protect_route(request, UserType.DOCTOR)
    if response: return response
    patients = RoleBasedUser.objects.filter(isDoctor = False)
    table_data = json.dumps([serialize_user(patient) for patient in patients])
    return render(request, "patients.html", {"table_data": table_data, "active": "patients"})