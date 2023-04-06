from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")
        labels = {
            "first_name": _("Firstname"),
            "last_name": _("Lastname"),
            "email": _("Email"),
            "password1": _("Password"),
            "password2": _("Confirm Password"),
        }
