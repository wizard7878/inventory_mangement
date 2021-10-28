from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if(user is None):
            context = {"Error","Invalid username or password"}
            return render(request,"accounts/logout.html",context=context)
        login(request,user)
        return redirect("/")
    return render(request,"accounts/login.html",{})

def logout_view(request):
    return render(request,"accounts/logout.html",{})


def register_view(request):
    return render(request,"accounts/register.html",{})