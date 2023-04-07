from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_pic = models.ImageField(
        null=True, blank=True, default="default_user_image.jpg"
    )
    user = models.OneToOneField(
        User, null=True, related_name="profile_user", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
