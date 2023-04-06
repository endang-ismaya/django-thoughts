from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from app_journal import models
from app_journal.forms import TaskForm, RegisterForm, LoginForm


def home(request):
    return render(request, "index.html")


# ---------------
# Users
# ---------------
def user_logout(request):
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect(reverse("app_journal:login"))


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, ("You have been logged in."))
                return redirect(reverse("app_journal:dashboard"))
            else:
                messages.warning(request, ("Error logging In - Please try it again."))
                return redirect(reverse("app_journal:login"))

        context = {
            "form": form,
        }
        return render(request, "login.html", context)

    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.POST.get("email")
            instance.first_name = instance.first_name.lower()
            instance.last_name = instance.last_name.lower()
            instance.save()

            return redirect(reverse("app_journal:home"))
    else:
        form = RegisterForm()

    context = {"form": form}

    return render(request, "register.html", context)


def register_success(request):
    return render(request, "register_success.html")


# ---------------
# Task
# ---------------
def tasks(request):
    tasks = models.Task.objects.order_by("-created_at")
    context = {"tasks": tasks}

    return render(request, "tasks.html", context)


def add_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse("app_journal:tasks"))

    context = {
        "form": form,
    }
    return render(request, "add_task.html", context)


def update_task(request, pk):
    task = models.Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect(reverse("app_journal:tasks"))

    context = {
        "form": form,
    }

    return render(request, "update_task.html", context)


def delete_task(request, pk):
    task = models.Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect(reverse("app_journal:tasks"))

    context = {"task": task}

    return render(request, "delete_task.html", context)


# ---------------
# Dashboard
# ---------------
@login_required(login_url="app_journal:login")
def dashboard(request):
    return render(request, "dashboard.html")
