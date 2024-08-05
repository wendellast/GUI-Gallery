from django.views.generic.list import ListView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.views.generic.list import ListView
from . import models

from . form import MusicForm

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
    model = models.Music
    form_class = MusicForm
    template_name = 'createMusic.html'
    success_url = reverse_lazy('gui:update-music')  

    
    
    def form_valid(self, form):
        form.instance.user = self.request.user  #
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_music'] = models.Music.objects.filter(user=self.request.user)
        return context
   
    

class MusicDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Music
    success_url = reverse_lazy('gui:update-music')
    
    
from django.http import JsonResponse
from .models import Music
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View

@method_decorator(login_required, name='dispatch')
class MusicDataView(View):
    def get(self, request, *args, **kwargs):
        music_entries = Music.objects.filter(user=request.user)
        music_list = [
            {
                'title': music.audio_file.name.split('/')[-1].split('.')[0],  # Extract title from filename
                'audio_url': music.audio_file.url,
                'cover_url': music.gallery.image.url if music.gallery else 'default_cover.jpg'  # Use a default cover if no gallery image
            }
            for music in music_entries
        ]
        return JsonResponse(music_list, safe=False)