from django.urls import path

from . import views

app_name = "userauths"


urlpatterns = [
    path("login/", views.PageLogin.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("logout/", views.logout_view, name="logout"),
]
