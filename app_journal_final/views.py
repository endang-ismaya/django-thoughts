from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="app_user:login")
def dashboard(request):
    return render(request, "app_journal_final/dashboard.html")


def index(request):
    return render(request, "index.html")
