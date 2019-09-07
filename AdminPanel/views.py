from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from AdminPanel.serializers import *

from AdminPanel.models import *
from django.shortcuts import render
from rest_framework.views import APIView,Response
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token

from Jobportal.global_variables import *

# Create your views here.
from employer.serializers import *

def index(request):
    return HttpResponse('Welcome to job portal')

class ListUsers(ListAPIView):


    serializer_class = ListUsersSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

