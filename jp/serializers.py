from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer

from AdminPanel.models import *

from django.contrib.auth import authenticate, get_user_model



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    details = serializers.SerializerMethodField()

    class Meta:
        model = Images
        fields = '__all__'

    def get_user(self, obj):
        print(obj.userid.id)
        user_instance = User.objects.get(id=obj.userid.id)
        response = UserSerializer(user_instance)
        return response.data

    def get_details(self, obj):
        print(obj.userid)
        user_details = UserDetails.objects.get(userid=obj.userid.id)
        response = UserDetailsSerializer(user_details)
        return response.data

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetails
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    UserDetails = UserDetailsSerializer(read_only=True)

    class Meta:
        model = UserDetails
        fields = '__all__'

