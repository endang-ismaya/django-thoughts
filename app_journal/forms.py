from django.forms import ModelForm
from app_journal.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
        )
