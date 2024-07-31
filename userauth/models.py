import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    username = models.CharField(max_length=100, unique=False)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    image_user_profile = models.ImageField(
        upload_to="user/profile/%Y/%m/", blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.username


def user_directory_path(instace, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s" % (instace.id, ext)

    return "user_{0}/{1}".format(instace.user.id, filename)
