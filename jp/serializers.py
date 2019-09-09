from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer

from AdminPanel.models import *

from django.contrib.auth import authenticate, get_user_model



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetails
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    UserDetails = UserDetailsSerializer(read_only=True)

    class Meta:
        model = UserDetails
        fields = '__all__'

