from django.urls import path
from app_user import views

app_name = "app_user"

urlpatterns = [
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("delete/", views.user_delete, name="delete"),
    path("profile/update", views.user_profile_update, name="profile_update"),
]
