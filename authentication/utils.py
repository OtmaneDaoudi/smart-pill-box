from django.shortcuts import redirect
from enum import Enum

class UserType(Enum):
    DOCTOR = 1
    PATIENT = 2

def protect_route(request, allow: UserType) -> None:
    user = request.user
    if not user.is_authenticated: return redirect("authentication:login")
    # admins are not meant to access the site
    elif user.is_superuser: return redirect("/admin")
    elif (user.rolebaseduser.isDoctor and allow == UserType.PATIENT) \
        or (not user.rolebaseduser.isDoctor and allow == UserType.DOCTOR):
        return redirect("authentication:login")