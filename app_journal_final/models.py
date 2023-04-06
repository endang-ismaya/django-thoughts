from django.db import models
from django.contrib.auth.models import User


class Thought(models.Model):
    title = models.CharField(max_length=85)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    poster = models.ForeignKey(
        User, max_length=10, on_delete=models.SET_NULL, null=True, related_name="poster"
    )
