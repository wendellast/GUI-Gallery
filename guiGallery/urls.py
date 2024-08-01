from allauth.socialaccount.providers.google.urls import \
    urlpatterns as google_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path

social_urlpatterns = [
    path("", include(google_urlpatterns)),
]
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("gui.urls")),
    path("user/", include("userauth.urls")),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
