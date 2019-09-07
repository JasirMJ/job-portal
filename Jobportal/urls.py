"""Jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from jp import views as jpviews



urlpatterns = [
    path('', include('AdminPanel.urls')),
    path('admin/', admin.site.urls),
    path('jobportal/', include('jp.urls') ,name = "register"),
    # url(r'^api-auth/', include('rest_framework.urls')),

    path('register/', jpviews.Register.as_view() ,name = "register"),
    path('index/', jpviews.Home.as_view() ,name = "home"),
    path('login/', jpviews.LoginView.as_view(),name = "login"),
]
