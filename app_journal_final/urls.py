from django.urls import path
from app_journal_final import views

app_name = "app_journal_final"

urlpatterns = [
    path("", views.journals, name="journals"),
]
