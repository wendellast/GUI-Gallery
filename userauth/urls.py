from django.urls import path

from . import views

app_name = "userauths"


urlpatterns = [
    path("login/", views.PageLogin.as_view()),
    path("register/", views.RegisterView.as_view(), name="register"),
]
