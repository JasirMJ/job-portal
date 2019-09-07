from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(),name = "home"),
    path('login-fre/', views.LoginView.as_view(),name = "login-emp"),

    path('image-upload', views.ImageUpload.as_view(),name = "image-upload"),
]