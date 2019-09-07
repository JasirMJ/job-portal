from django.conf.urls.static import static
from django.urls import path

from Jobportal import settings
from . import views


urlpatterns = [
    path('', views.Home.as_view(),name = "home"),

    path('image-upload/', views.ImageUpload.as_view(),name = "image-upload"),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)