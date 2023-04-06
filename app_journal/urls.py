from django.urls import path
from . import views

app_name = "app_journal"
urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("tasks/<int:pk>/update/", views.update_task, name="update_task"),
    path("tasks/<int:pk>/delete/", views.delete_task, name="delete_task"),
    path("register/", views.register, name="register"),
]
