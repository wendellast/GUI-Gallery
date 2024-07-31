import uuid

from django.db import models
from django.utils.html import format_html

from userauth.models import User



class GuiGallery(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gui_gallery")
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ImagesGuiGallery(models.Model):
    id_photo = models.ForeignKey(
        GuiGallery, on_delete=models.CASCADE, related_name="images_gui_gallery"
    )
    image_1 = models.ImageField(upload_to="gallery/imgs/%Y/%m/")
    image_2 = models.ImageField(upload_to="gallery/imgs/%Y/%m/")
    image_3 = models.ImageField(upload_to="gallery/imgs/%Y/%m/")
    image_4 = models.ImageField(upload_to="gallery/imgs/%Y/%m/")
