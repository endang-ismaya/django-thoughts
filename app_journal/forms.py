from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app_journal.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
        )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")
