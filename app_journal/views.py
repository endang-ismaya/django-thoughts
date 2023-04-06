from django.shortcuts import render
from app_journal import models


# Create your views here.
def register(request):
    return render(request, "register.html")


def home(request):
    return render(request, "index.html")


def tasks(request):
    tasks = models.Task.objects.order_by("-created_at")
    context = {"tasks": tasks}

    return render(request, "tasks.html", context)
