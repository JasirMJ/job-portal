from rest_framework import serializers, exceptions
from AdminPanel.models import *

from django.contrib.auth import authenticate, get_user_model


#
# class LoginSerializer(serializers.Serializer):
#     mobile = serializers.CharField()
#     # password = serializers.CharField()
#     def validate(self,data):
#         print("info ------------------- Authentication started")
#         mobile = data.get('mobile','')
#         # password = data.get('password','')
#         print("info ------------------- username and password recieved")
#         print("info ------------------- username ",mobile," and password ,password ,recieved")
#         if mobile :
#             print("info ------------------- username n password forwaring to authnticate")
#             try:
#                 # user = authenticate(username=username)
#                 user = User.objects.filter(mobile=mobile).first()
#                 print("user  : ",user)
#
#             except Exception as e:
#                 print("Excepction ",e)
#             if user:
#                 print("info ------------------- authnticated sucessfully")
#
#                 if user.is_active:
#                     data['user']=user
#                 else:
#                     msg="user is deactivated"
#                     raise exceptions.ValidationError(msg)
#             else:
#                 msg="unable to login with given credentials"
#                 # return Response({'Message':msg})
#                 raise exceptions.ValidationError(msg)
#         else:
#             msg ="validation error"
#
#             raise exceptions.ValidationError(msg)
#         return data

# class ImageUploadSerializer(serializers.ModelSerializer):
#     # obj = User()
#     class Meta:
#
#         model = Images
#         fields = ['category','file']

    # def get_parameter_name(self, obj):
    #     return str(obj.userid.parameter_name)