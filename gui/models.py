from django.db import models

from userauth.models import User


class GuiGallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    profile_image = models.ImageField(
        upload_to="profileImage/%Y/%m/", blank=True, null=True
    )
    image = models.ImageField(upload_to="galleryPhotos/%Y/%m/", blank=False, null=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
