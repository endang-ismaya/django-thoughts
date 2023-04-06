"""
Project URLs
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("journals/v1/", include("app_journal.urls")),
    path("journals/v2/", include("app_journal_final.urls")),
    path("users/", include("app_user.urls")),
]
