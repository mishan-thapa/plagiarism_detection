from django.contrib import admin
from django.urls import path

from first_app import views
from .views import extract_paragraphs

urlpatterns = [
        path("", views.plag_check, name="plag_check"),
        path('upload_pdf', views.upload_pdf, name='upload_pdf'),
        path("home", views.home, name="home"),
        path("check", views.check, name="check"),
        path("upload", views.upload, name="upload"),
        path("thesis_upload_page", views.thesis_upload_page, name="thesis_upload_page"),
        path("thesis_upload", views.thesis_upload, name="thesis_upload"),
        path("try", views.tryy, name="tryy"),
        path("view_thesis",views.view_thesis, name="view_thesis"),
        path('upload1/', extract_paragraphs, name='extract_paragraphs'),
]

#