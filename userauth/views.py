from django.views import View
from django.views.generic.list import ListView

from . import models


class PageLogin(ListView):
    model = models.User
    template_name = "sign-in.html"
    context_object_name = "userauths"
