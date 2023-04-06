from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User

from app_journal import models
from app_journal.forms import TaskForm, RegisterForm


def home(request):
    return render(request, "index.html")


# ---------------
# Users
# ---------------
def register(request):
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
