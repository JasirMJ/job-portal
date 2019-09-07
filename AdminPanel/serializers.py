from rest_framework import serializers, exceptions
from AdminPanel.models import *

from django.contrib.auth import authenticate, get_user_model



class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'email']
        fields = '__all__'