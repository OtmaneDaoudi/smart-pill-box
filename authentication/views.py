from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate


# Create your views here.
def login_view(request):
    # Admins are not meant to access this page
    if request.user.username == "admin":
        return redirect("/admin")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            destination = "doctor/" if user.rolebaseduser.isDoctor else "patient/"
            # return redirect(destination)
            return HttpResponse(f"{destination}")
        return render(request, "login.html", {"error": True})
    return render(request, "login.html")