from django.shortcuts import render
from medication.models import Prescription, Intake
from authentication.utils import protect_route, UserType
import datetime

# Create your views here.
def get_prescriptions(request):
    response = protect_route(request, UserType.PATIENT)
    if response: return response

    patient_id = request.user.rolebaseduser.id

    def resolve_tasks(prescriptions):
        if not prescriptions: return [], []

        done = []
        todo = []
        for prescription in prescriptions:
            curr_day_intake = prescription.intake_set.filter(
                # prescription=prescription.id,
                date = datetime.date.today()
            )

            if curr_day_intake: 
                done.append(
                    {
                        "medication": prescription.medication.name,
                        "duration": prescription.duration,
                        "isAfterFood": prescription.isAfterFood,
                        "takenFor": prescription.intake_set.count() + 1
                    }
                )
            else:
                todo.append(
                    {
                        "id": prescription.id,
                        "medication": prescription.medication.name,
                        "duration": prescription.duration,
                        "takenFor": prescription.intake_set.count() + 1,
                        "isAfterFood": prescription.isAfterFood
                    }
                )
        return todo, done

    morning_prescriptions = Prescription.objects.filter(patient=patient_id, period="M")
    afternoon_prescriptions = Prescription.objects.filter(patient=patient_id, period="A")
    evening_prescriptions = Prescription.objects.filter(patient=patient_id, period="E")

        
    morning_to_do_prescriptions, morning_done_intake = resolve_tasks(morning_prescriptions)
    afternoon_to_do_prescriptions, afternoon_done_intake = resolve_tasks(afternoon_prescriptions)
    evening_to_do_prescriptions, evening_done_intake = resolve_tasks(evening_prescriptions)

    context = {
        "active": "prescription",
        "patient_id": patient_id,
        "active": "prescription",
        "morning_to_do_prescriptions": morning_to_do_prescriptions,
        "morning_done_intake": morning_done_intake,
        "afternoon_to_do_prescriptions": afternoon_to_do_prescriptions,
        "afternoon_done_intake": afternoon_done_intake,
        "evening_to_do_prescriptions": evening_to_do_prescriptions,
        "evening_done_intake": evening_done_intake
    }

    return render(request, "todo.html", context=context)