from django.shortcuts import render, HttpResponse
from authentication.utils import protect_route, UserType, redirect
from .models import Medication, Prescription, Intake
from authentication.models import RoleBasedUser
import json, datetime

def serialize_medication(medication: Medication):
    if not medication: return {}
    return [
        medication.id,
        medication.name,
        medication.instructions
    ]

# Create your views here.
def get_medications(request):
    reponse = protect_route(request, UserType.DOCTOR)
    if reponse: return reponse

    medications = Medication.objects.all()
    table_data = json.dumps([serialize_medication(med) for med in medications])
    return render(request, "medications.html", {"active": "medications", "table_data": table_data})

def delete_medication(request, medication_id):
    reponse = protect_route(request, UserType.DOCTOR)
    if reponse: return reponse

    medication = Medication.objects.get(id=medication_id)
    medication.delete()
    
    medications = Medication.objects.all()
    table_data = json.dumps([serialize_medication(med) for med in medications])
    return render(request, "medications.html", {"active": "medications", "table_data": table_data})

def add_new(request):
    reponse = protect_route(request, UserType.DOCTOR)
    if reponse: return reponse

    name = request.POST["name"]
    instructions = request.POST["instructions"]
    Medication(name=name, instructions=instructions).save()
    return redirect("medications:meds")

def get_prescription(request, patient_id):
    reponse = protect_route(request, UserType.DOCTOR)
    if reponse: return reponse

    medications = Medication.objects.all()
    # tasks
    morning_tasks = Prescription.objects.filter(patient=patient_id, period="M")
    afternoon_tasks = Prescription.objects.filter(patient=patient_id, period="A")
    evening_tasks = Prescription.objects.filter(patient=patient_id, period="E")

    context = {
        "active": "prescription",
        "medications": medications,
        "patient_id": patient_id,
        "morning_tasks": morning_tasks,
        "afternoon_tasks": afternoon_tasks,
        "evening_tasks": evening_tasks
    }

    return render(request, "prescriptions.html", context)

def update_prescription(request):
    medication_id = request.POST["medication"]
    period = request.POST["period"]
    isAfterFood = True if request.POST.get("isAfterFood", "off") == "on" else False
    patient_id = request.POST.get("patient_id", None)
    doctor_id = request.user.rolebaseduser.id
    print(f"doctor_id", {doctor_id})
    duration = request.POST["duration"]
    # Persist new prescription
    Prescription(
        doctor = RoleBasedUser.objects.get(id=doctor_id),
        patient= RoleBasedUser.objects.get(id=patient_id),
        medication = Medication.objects.get(id = medication_id),
        period=period,
        isAfterFood=isAfterFood,
        duration=duration
    ).save()

    return redirect(f"/medication/prescription/{patient_id}")

def delete_prescription(request):
    prescription_id = request.POST["prescription_id"]
    patient_id = request.POST["patient_id"]
    Prescription.objects.get(id=prescription_id).delete()
    return redirect(f"/medication/prescription/{patient_id}")


def daily_intake(request):
    prescription_id = request.POST["prescription_id"]

    now = datetime.datetime.now()
    period = None
    if 6 <= now.hour <= 12: period = "M"
    elif 12 < now.hour <= 18: period = "A"
    else: period = "E"
    
    newIntake = Intake(
        prescription=Prescription.objects.get(id=prescription_id),
        date = datetime.date.today(),
        period = period
    )
    newIntake.save()

    return redirect("patients:todo")