from django.urls import path
from app_journal_final import views

app_name = "app_journal_final"

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("thoughts/", views.list_thought, name="list_thought"),
    path("thoughts/<int:pk>/update", views.update_thought, name="update_thought"),
    path("thoughts/<int:pk>/delete", views.delete_thought, name="delete_thought"),
    path("thoughts/add/", views.add_thought, name="add_thought"),
]
