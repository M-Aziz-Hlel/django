from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm, LoginForm


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignupForm()

    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )

            if user:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})