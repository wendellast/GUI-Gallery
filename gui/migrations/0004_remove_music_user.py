# Generated by Django 5.0.7 on 2024-08-05 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gui", "0003_remove_guigallery_music_music"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="music",
            name="user",
        ),
    ]
