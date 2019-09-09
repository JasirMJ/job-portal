import os

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models.expressions import RawSQL
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from django.db import connection

from AdminPanel.models import *
from django.shortcuts import render
from rest_framework.views import APIView,Response
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token

from Jobportal.global_variables import *

# Create your views here.
from employer.serializers import *
from jp.serializers import *


def check_empty(items):
    print(items)
    for x in items:
        print(INFO,x)
        if x == "" or not x:
            msg = "required "+ str(x)
            return msg
        print(INFO, x,":", x)
    return 1


class Register(APIView):

    def get(self, request):
        return Response(
            {
                STATUS: True,
            }
        )

    def post(self, request):

        # fire_base = self.request.POST.get('fire_base','')
        username = self.request.POST.get('username')
        email = self.request.POST.get('email')
        mobile = self.request.POST.get('mobile')
        # pin = self.request.POST.get('pin')
        latitude = self.request.POST.get('latitude')
        longitude = self.request.POST.get('longitude')
        # password = self.request.POST.get("password")

        result = check_empty([username,email,mobile,latitude,longitude])
        print(INFO,"result :",result)
        if result == 1:

            try:
                uname_check_obj = User.objects.filter(username=username)
                if uname_check_obj.exists():
                    uname = uname_check_obj.first()
                    return Response(
                        {
                            STATUS: False,
                            MESSAGE: "username " + str(uname) + " already exist"
                        }
                    )

                email_check_obj = User.objects.filter(email=email)
                if email_check_obj.exists():
                    email = email_check_obj.first().email
                    return Response(
                        {
                            STATUS: False,
                            MESSAGE: "email " + str(email) + " already exist"
                        }
                    )

                mobile_check_obj = User.objects.filter(mobile=mobile)

                if mobile_check_obj.exists():
                    mobile = mobile_check_obj.first().mobile
                    return Response(
                        {
                            STATUS: False,
                            MESSAGE: "mobile " + str(mobile) + " already exist"
                        }
                    )
            except Exception as E:
                return Response(
                    {
                        STATUS: False,
                        "Excepction": str(E)
                    }
                )

            try:
                obj = User()
                obj.username = username
                obj.email = email
                # obj.password = make_password(password)
                obj.mobile = mobile

                obj.save()

                ud_obj = UserDetails()
                ud_obj.mobile = mobile
                ud_obj.userid = obj
                ud_obj.username = username
                ud_obj.email = email
                # ud_obj.pin = pin

                # ud_obj.latitude = latitude
                # ud_obj.longitude = longitude

                # emp_obj.firebase = fire_base
                ud_obj.save()
                return Response(
                    {
                        STATUS: True,
                    }
                )

            except Exception as e:
                print(ERROR, e)
                obj.delete()
                return Response(
                    {
                        STATUS: False,
                        "Excepction": str(e),

                    }
                )




        else:
            return Response(
                {
                    STATUS: False,
                    MESSAGE: " required :  username, email, mobile, latitude, longitude",
                }
            )

        # if fire_base == "" or not fire_base:
        #     msg = "required fire_base"
        #     return Response(
        #         {
        #             MESSAGE: msg,
        #             STATUS: False,
        #         }
        #     )
        # else :
        # print(INFO, "fire_base ", fire_base)



class LoginView(APIView):
    def get(self):
        return Response(
            {
                STATUS:'post method is needed'
            }
        )

    def post(self,request):     #verifying using serializer
        serializer = LoginSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            print(INFO,"user : ",user)
            print(django_login(request,user))
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'Token':token.key,
                },
                status=200
            )
        except Exception as e:
            print("Excepction occured ################### : ",e)
            return Response(
                {
                    'status':False,
                    'Message':'Invalid user',
                }
            )

class Home(APIView):
    def get(self,request):
        return Response(
            {
                STATUS:True,
                MESSAGE: "This is a home page",
            }
        )

    def post(self,request):

        return Response(
            {
                STATUS: True,
                MESSAGE:"This is a home page",
            }
        )

class ImageUpload(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self,request):
        obj = Images.objects.filter(userid=self.request.user)


        return Response(
            {
                STATUS:True,
                MESSAGE:"this is a get request",
            }
        )

    def post(self, request, *args, **kwargs):
        img_obj = Images()
        if request.FILES:
            print("file field posted")
            image_name = request.FILES['profile'].name  #
            file = request.FILES['profile']
            fs = FileSystemStorage()
            filename = fs.save(image_name, file)
            uploaded_file_url = fs.url(filename)
            print(INFO,"uploaded file url :", uploaded_file_url)
            print(INFO,"image name", image_name)
            print(INFO,"profile", file)
            img_obj.file = uploaded_file_url
            img_obj.category = "profile pic"
            img_obj.userid = self.request.user
            img_obj.save()

            return Response(
                {
                    STATUS: True,
                    MESSAGE:"Image uploaded",

                }
            )
        else:
            print(INFO,"file not posted")

            return Response(
                {
                    STATUS:False,
                    MESSAGE: "no file posted",
                }
            )


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Profile(ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ImageSerializer

    def get_queryset(self):
        obj = Images.objects.filter(userid = self.request.user.id)
        return obj

    # def get(self,request):
        user_obj = User.objects.filter(id=self.request.user.id).first()

        details_obj = UserDetails.objects.filter(userid=self.request.user.id).first()
        img_obj = Images.objects.filter(userid=self.request.user.id).first()


        u_dict = {
            'username':user_obj.username,
            'mobile':user_obj.mobile,
        }

        return Response(
            {
                STATUS:True,
                'username': user_obj.username,
                'mobile': user_obj.mobile,
                'profile':str(img_obj.file),
                'profile':BASE_DIR+str(img_obj.file),




                # 'details':user_details_data,
                # 'image':image_data,
            }
        )
    def post(self,request):

        #updat goes here
        return Response(
            {
                STATUS:True,
            }
        )

class OnclickFreelancer(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self,request):
        return Response({STATUS:True,MESSAGE:"this is get"})
        # ud_obj = UserDetails.objects.filter(userid=self.request.user.id).first()
        # if ud_obj.is_freelancer == 1:
        #     msg = "user is free freelancer"
        #     return Response(
        #         {
        #             STATUS: True,
        #             MESSAGE: msg,
        #         }
        #     )
        # else:
        #     msg = "user is not freelancer"
        #     return Response(
        #         {
        #             STATUS:True,
        #             MESSAGE:msg,
        #         }
        #     )
    def post(self,request):
        ud_obj = UserDetails.objects.filter(userid=self.request.user.id).first()
        if ud_obj.is_freelancer == 1:
            msg = "user is free freelancer"
            return Response(
                {
                    STATUS: True,
                    MESSAGE: msg,
                }
            )
        else:
            msg = "user is not freelancer"
            return Response(
                {
                    STATUS: True,
                    MESSAGE: msg,
                }
            )

# list all skill api
#list all freelancer api
#rate freelancer ,who has completed the work ie accepted
#