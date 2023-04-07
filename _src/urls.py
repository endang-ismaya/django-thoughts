"""
Project URLs
"""
from django.contrib import admin
from django.urls import path, include

# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app_journal_final.urls")),
    path("users/", include("app_user.urls")),
    path("journals/v1/", include("app_journal.urls")),
]
