from django import forms
from app_journal_final.models import Thought


class ThoughtPostForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ("title", "content")
        exclude = ("poster",)


class ThoughtUpdateForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ("title", "content")
        exclude = ("poster",)
