from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import LoginForm, RegisterForm, UserEditForm
from django.contrib.auth.models import User



# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect("home_app:home_page")
    if request.method == "POST":
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = User.objects.get(username=form.cleaned_data["username"])
            login(request, user)
            messages.success(request, "✅ خوش آمدید! شما با موفقیت وارد شدید.","success")
            return redirect("home_app:home_page")
        else:
            messages.error(request, "❌ نام کاربری یا رمز عبور اشتباه است.","danger")
            return redirect("account_app:login_page")

    else:
        form = LoginForm()
    return render(request, "account_app/login.html", {"form":form})

def logout_page(request):
    logout(request)
    return redirect("home_app:home_page")

def registration_page(request):
    if request.user.is_authenticated:
        messages.success(request, "برای ثبت نام جدید ابتدا از حساب خارج شوید!", "warning")
        return redirect("home_app:home_page")
    if request.method == "POST":
        print("HELLO")
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            User.objects.create_user(username=user, password=password1)
            messages.success(request, "✅حساب کاربری شما با موفقیت ایجاد شد","success")
            return redirect("account_app:login_page")
        else:
            messages.error(request, "❌اطلاعات وارد شده صحیح نیست","danger")
            return render(request, "account_app/register.html", {"form":form})

    else:
        form = RegisterForm
    return render(request,"account_app/register.html", {"form":form})

def profile_page(request):
    form = UserEditForm(instance=request.user)
    if request.method == "POST":
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request,"account_app/profile.html",{"form":form})