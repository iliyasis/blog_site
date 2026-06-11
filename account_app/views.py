from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect("home_app:home_page")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "✅ خوش آمدید! شما با موفقیت وارد شدید.","success")
            return redirect("home_app:home_page")
        else:
            messages.error(request, "❌ نام کاربری یا رمز عبور اشتباه است.","danger")
            return redirect("account_app:login_page")

    return render(request, "account_app/login.html")

def logout_page(request):
    logout(request)
    return redirect("home_app:home_page")

def registration_page(request):
    return render(request,"account_app/register.html")