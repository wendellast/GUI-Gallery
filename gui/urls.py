
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.PagePetIndex.as_view())
]
