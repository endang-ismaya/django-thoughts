from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from app_journal_final.forms import ThoughtPostForm


# Create your views here.
@login_required(login_url="app_user:login")
def dashboard(request):
    return render(request, "app_journal_final/dashboard.html")


@login_required(login_url="app_user:login")
def add_thought(request):
    # initialize form
    form = None

    if request.method == "POST":
        form = ThoughtPostForm(request.POST)

        if form.isvalid():
            thought = form.save(commit=False)
            thought.poster = request.user
            thought.save()
            messages.success(request, "Thought added successfully.")
            return redirect(reverse("app_journal_final:dashboard"))
    else:
        form = ThoughtPostForm()

    context = {"form": form}
    return render(request, "app_journal_final/thought/add-thought.html", context)


def index(request):
    return render(request, "index.html")
