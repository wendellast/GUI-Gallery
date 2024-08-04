from django import forms
from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'artist', 'album', 'release_date', 'genre', 'audio_file', 'cover_image', 'description', 'gallery']
