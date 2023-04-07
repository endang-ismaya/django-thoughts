from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from app_journal_final.forms import ThoughtPostForm, ThoughtUpdateForm
from app_journal_final.models import Thought


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

        if form.is_valid():
            thought = form.save(commit=False)
            thought.poster = request.user
            thought.save()
            messages.success(request, "Thought added successfully.")
            return redirect(reverse("app_journal_final:list_thought"))
    else:
        form = ThoughtPostForm()

    context = {"form": form}
    return render(request, "app_journal_final/thought/add-thought.html", context)


@login_required(login_url="app_user:login")
def update_thought(request, pk):
    try:
        form = None
        thought = Thought.objects.get(pk=pk, poster=request.user)

        if request.method == "POST":
            form = ThoughtUpdateForm(request.POST, instance=thought)

            if form.is_valid():
                thought.save()
                messages.success(request, "Thought updated successfully.")
                return redirect(reverse("app_journal_final:list_thought"))
        else:
            form = ThoughtUpdateForm(instance=thought)

        context = {"form": form}
        return render(request, "app_journal_final/thought/update-thought.html", context)
    except Thought.DoesNotExist:
        messages.error(request, "Thought not found!.")
        return redirect(reverse("app_journal_final:list_thought"))


@login_required(login_url="app_user:login")
def list_thought(request):
    current_user = request.user
    thoughts = Thought.objects.all().filter(poster=current_user)

    context = {"thoughts": thoughts}
    return render(request, "app_journal_final/thought/list-thought.html", context)


@login_required(login_url="app_user:login")
def delete_thought(request, pk):
    try:
        thought = Thought.objects.get(pk=pk, poster=request.user)

        if request.method == "POST":
            thought.delete()
            messages.success(request, "Thought has been deleted")
            return redirect(reverse("app_journal_final:list_thought"))

        context = {"thought": thought}
        return render(request, "app_journal_final/thought/delete-thought.html", context)
    except Thought.DoesNotExist:
        messages.error(request, "Thought not found!.")
        return redirect(reverse("app_journal_final:list_thought"))


def index(request):
    return render(request, "index.html")
