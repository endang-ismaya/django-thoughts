from django.urls import path
from . import views

app_name = "app_journal"
urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
]
