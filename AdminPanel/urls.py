from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name = "index"),
    # path('register', views.Register.as_view(),name = "register"),
    path('users/',views.ListUsers.as_view(),name = "list users")
]