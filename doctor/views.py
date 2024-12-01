from django.shortcuts import render, HttpResponse, redirect
from authentication.models import RoleBasedUser

# Create your views here.
def get_patients(request):
    # redirect if not logged in as a doctor
    user = request.user
    if not user or not user.rolebaseduser.isDoctor: return redirect("authentication:login")
    
    patients = RoleBasedUser.objects.get(isDoctor = False)
    return HttpResponse("They don't beleive in us, but god did")