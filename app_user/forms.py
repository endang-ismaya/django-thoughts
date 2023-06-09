from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from app_user.models import Profile


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


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class UpdateUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = ("first_name", "last_name")
        exclude = ("password1", "password2", "username")


class UpdateProfilePictureForm(forms.ModelForm):
    profile_pic = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Profile
        fields = ("profile_pic",)
        labels = {"profile_pic": ""}
