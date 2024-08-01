from django.urls import path

from . import views

app_name = "gui"

urlpatterns = [
    path("", views.PagePetIndex.as_view(), name="index"), 
    ]
