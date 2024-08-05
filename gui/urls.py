from django.urls import path

from . import views

app_name = "gui"

urlpatterns = [
    path("", views.PageIndex.as_view(), name="index"), 
    path("upload-image/", views.PageNewBook.as_view(), name="update-image"),
    path("upload-music/", views.PageNewMusic.as_view(), name="update-music"),
    path('delete/<int:pk>/', views.MusicDeleteView.as_view(), name='delete-music'),
    ]
