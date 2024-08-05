from django import forms
from .models import Music, GuiGallery

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['audio_file']
    