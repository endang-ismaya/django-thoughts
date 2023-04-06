from django.shortcuts import redirect, render
from django.urls import reverse
from app_journal import models
from app_journal.forms import TaskForm


# Create your views here.
def register(request):
    return render(request, "register.html")


def home(request):
    return render(request, "index.html")


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
