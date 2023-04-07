from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from app_user.forms import (
    RegistrationForm,
    LoginForm,
    UpdateUserForm,
    UpdateProfilePictureForm,
)
from app_user.models import Profile


def user_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.POST.get("email")
            instance.first_name = instance.first_name.lower()
            instance.last_name = instance.last_name.lower()

            # add profile
            instance.save()

            # after registration successful, login and redirect to dashboard
            # user = authenticate(
            #     request, username=instance.username, password=instance.password
            # )
            Profile.objects.create(user=instance)
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


@login_required(login_url="app_user:login")
def user_logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, ("You have been logged out."))
        return redirect(reverse("app_user:login"))

    return render(request, "app_user/login.html")


@login_required(login_url="app_user:login")
def user_profile_update(request):
    try:
        form = None

        if request.method == "POST":
            form = UpdateUserForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully.")
                return redirect(reverse("app_user:profile_update"))
        else:
            form = UpdateUserForm(instance=request.user)

        form_picture = UpdateProfilePictureForm()
        user_profile = Profile.objects.get(user=request.user)
        context = {
            "form": form,
            "profile_pic": user_profile.profile_pic,
            "form_picture": form_picture,
        }
        return render(request, "app_user/profile_update.html", context)
    except Exception:
        messages.error(request, "Something went wrong!.")
        return redirect(reverse("app_journal_final:dashboard"))


@login_required(login_url="app_user:login")
def user_profile_image_update(request):
    try:
        form = None

        if request.method == "POST":
            profile = Profile.objects.get(user=request.user)
            form = UpdateProfilePictureForm(
                request.POST, request.FILES, instance=profile
            )

            if form.is_valid():
                form.save()
                messages.success(request, "Image profile updated successfully.")
                return redirect(reverse("app_user:profile_update"))
        else:
            form = UpdateUserForm(instance=request.user)

        form_picture = UpdateProfilePictureForm()
        user_profile = Profile.objects.get(user=request.user)
        context = {
            "form": form,
            "profile_pic": user_profile.profile_pic,
            "form_picture": form_picture,
        }
        return render(request, "app_user/profile_update.html", context)
    except Exception:
        messages.error(request, "Something went wrong!.")
        return redirect(reverse("app_journal_final:dashboard"))


@login_required(login_url="app_user:login")
def user_delete(request):
    try:
        if request.method == "POST":
            delete_user = User.objects.get(username=request.user)
            delete_user.delete()
            return redirect(reverse("app_user:login"))

        return render(request, "app_user/delete_user.html")

    except Exception:
        messages.error(request, "Something went wrong!.")
        return redirect(reverse("app_journal_final:dashboard"))
