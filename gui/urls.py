from django.urls import path

from . import views

app_name = "gui"

urlpatterns = [
    path("", views.PageIndex.as_view(), name="index"), 
    path("upload-image/", views.PageNewBook.as_view(), name="update-image")
    ]
