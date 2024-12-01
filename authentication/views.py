from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def login_view(request):
    # Admins are not meant to access this page
    if request.user.username == "admin":
        return redirect("/admin")
    
    form = None
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            user_type = "doctor" if user.rolebaseduser.isDoctor else "patient"
            return HttpResponse(user_type)
    else: form = AuthenticationForm()
    return render(request, "login.html", {"form": form})