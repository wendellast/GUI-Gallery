from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.GuiGallery)
class GuiAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
    )
    