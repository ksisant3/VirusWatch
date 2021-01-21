from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.password_validation import validate_password, ValidationError


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print(response.POST)
        try:
            validate_password(response.POST.get("password2"))
            if form.is_valid():
                form.save()
                return redirect("/home") 
            else:
                form = RegisterForm()
                return render(response, "register/register.html", {"form": form})
        
        except ValidationError as e:
            print(str(e))