from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # password reset
    # 1. Allow us to enter our email in order to receive a password reset link
    path(
        "reset_password/", auth_views.PasswordResetView.as_view(), name="reset_password"
    ),
    # 2. Show a success message stating that an email was successfully sent to our password
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    # 3. Send a link to our email, so that we can reset our password
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    # 4. Show message stating that our password was successfully changed
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
