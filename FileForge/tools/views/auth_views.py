"""Authentication views — login, signup, logout."""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next", "/")
            return redirect(next_url)
        else:
            error = "Invalid username or password."
    return render(request, "auth/login.html", {"error": error})


def signup_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")

        if not username or not password:
            error = "Username and password are required."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        elif password != password2:
            error = "Passwords do not match."
        elif User.objects.filter(username=username).exists():
            error = "That username is already taken."
        elif email and User.objects.filter(email=email).exists():
            error = "An account with that email already exists."
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            login(request, user)
            return redirect("/")
    return render(request, "auth/signup.html", {"error": error})


def logout_view(request):
    logout(request)
    return redirect("/")
