from django.shortcuts import render, redirect
from django.urls import reverse
from app_user.forms import RegistrationForm


def user_register(request):
    if request.method == "POST":
        print(request.POST)
        form = RegistrationForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.POST.get("email")
            instance.first_name = instance.first_name.lower()
            instance.last_name = instance.last_name.lower()
            instance.save()

            return redirect(reverse("app_journal:home"))

        context = {"form": form}

        return render(request, "app_user/register.html", context)

    else:
        form = RegistrationForm()
        context = {"form": form}
        return render(request, "app_user/register.html", context)


def user_login(request):
    pass


def user_logout(request):
    pass
