from django.urls import path
from .views import import_page, importer_app_check

urlpatterns = [
    path("", import_page, name="import"),
    path("appcheck/", importer_app_check, name="ImportCheck")
]