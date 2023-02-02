from django.contrib import admin
from django.urls import path

from first_app import views

urlpatterns = [
        path("", views.home, name="home"),
        path("check", views.check, name="check"),
        path("upload", views.upload, name="upload"),
        path("try", views.tryy, name="tryy")
]

