"""
URL configuration for AuthorsBooksDRFProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from AuthorsBooksDRFApp.views import AuthorViewSet, GenreViewSet, BookViewSet, AllDataView


# Роутеры для перехода на соответствующие страницы (DRF)
router = routers.DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="authors")
router.register(r"genres", GenreViewSet, basename="genres")
router.register(r"books", BookViewSet, basename="books")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("AuthorsBooksDRFApp.urls", namespace="AuthorsBooksDRFApp")),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")), # ЭТО НЕ ПОЛУЧИЛОСЬ РЕАЛИЗОВАТЬ ПОКА ЧТО
    path("all-data/", AllDataView.as_view(), name="all-data"), # И ЭТО ТОЖЕ
]
