from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.http import require_POST

def login_validation(request):
    pass

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST["username"], password=request.POST["password"]+"my_salt")
        if user is not None:
            auth.login(request, user)
            messages.success(request, "وارد شدید")
            return redirect("base:index")
        elif User.objects.filter(username=request.POST["username"]).exists():
            messages.error(request, "رمز عبور را صحیح وارد کنید")
        else:
            messages.error(request, "نام کاربری وارد شده ثبت نشده است")
        return redirect("accounts:login")
    elif request.method == "GET":
        return render(request, "accounts/login.html")


def reg_validation(request):
    if User.objects.filter(username=request.POST["username"]).exists():
        messages.error(request, "نام کاربری وارد شده قبلا انخاب شده است!")
    if User.objects.filter(email=request.POST["email"]).exists():
        messages.error(request, "این ایمیل در سیستم موجود است!")
    if request.POST["password"] != request.POST["confirm_password"]:
        messages.error(request, "رمز های عبور وارد شده یکسان نیستند!")
    return request


def register(request):
    if request.method == "POST":
        if request != reg_validation(request):
            request = reg_validation(request)
        else:
            user = User.objects.create_user(first_name=request.POST["first_name"], 
                                            last_name=request.POST["last_name"], username=request.POST["username"], 
                                            password=request.POST["password"]+"my_salt", 
                                            email=request.POST["email"])
            user.save()
            messages.success(request, "ثبت نام شما با موفقیت ثبت شد")
        return redirect("base:index")
    elif request.method == "GET":
        return render(request, "accounts/register.html")

@require_POST
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.info(request, "با موفقیت خارج شدید")
        return redirect("base:index")