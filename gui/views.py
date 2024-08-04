from django.views.generic.list import ListView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView
from . import models

class PageIndex(ListView):
    model = models.GuiGallery
    template_name = "index.html"
    context_object_name = "guigallery"

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = models.GuiGallery.objects.filter(user=user)
        else:
            return reverse_lazy("gui:index")
        return queryset



class PageNewBook(LoginRequiredMixin, CreateView):
    model = models.GuiGallery
    fields = ["title", "description", "image"]
    success_url = reverse_lazy("gui:index")
    template_name = "createImage.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PageNewBook, self).form_valid(form)
    
class PageNewMusic(LoginRequiredMixin, CreateView):
    model = models.GuiGallery
    fields = ["title", "description", "image"]
    success_url = reverse_lazy("gui:index")
    template_name = "createMusic.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PageNewBook, self).form_valid(form)