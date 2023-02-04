from decouple import config

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("valuator.urls")),
    path(config("URL_ADMIN_PATH"), admin.site.urls),
]