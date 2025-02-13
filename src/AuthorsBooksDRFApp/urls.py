from django.urls import path
from .views import index


app_name = "AuthorsBooksDRFApp"

urlpatterns = [
    path("", index, name="index"),
]
