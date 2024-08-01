from django.views.generic.list import ListView

from . import models


# Create your views here.
class PagePetIndex(ListView):
    model = models.GuiGallery
    template_name = "index.html"
    context_object_name = "guigallery"
