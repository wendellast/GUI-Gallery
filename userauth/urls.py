from django.urls import path

from . import views

app_name = "userauths"


urlpatterns = [
    path("login/", views.PageLogin.as_view()),
]
