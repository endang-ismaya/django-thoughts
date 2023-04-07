from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from app_user.forms import RegistrationForm, LoginForm


def user_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.POST.get("email")
            instance.first_name = instance.first_name.lower()
            instance.last_name = instance.last_name.lower()
            instance.save()

            # after registration successful, login and redirect to dashboard
            # user = authenticate(
            #     request, username=instance.username, password=instance.password
            # )
            login(request, instance)
            messages.success(
                request, "Registration successful, your account has been registered"
            )
            return redirect(reverse("app_journal_final:dashboard"))

        context = {"form": form}

        return render(request, "app_user/register.html", context)

    else:
        form = RegistrationForm()
        context = {"form": form}
        return render(request, "app_user/register.html", context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # messages.success(request, ("You have been logged in."))
                return redirect(reverse("app_journal_final:dashboard"))
            else:
                messages.warning(request, ("Error logging In - Please try it again."))
                return redirect(reverse("app_user:login"))

        context = {
            "form": form,
        }
        return render(request, "app_user/login.html", context)

    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "app_user/login.html", context)


@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, ("You have been logged out."))
        return redirect(reverse("app_user:login"))

    return render(request, "app_user/login.html")
