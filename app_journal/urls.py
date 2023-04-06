from django.urls import path
from . import views

app_name = "app_journal"
urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.tasks, name="tasks"),
    path("register/", views.register, name="register"),
]
