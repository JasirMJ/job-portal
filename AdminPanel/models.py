from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=10)
    

class EmployersDetails(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    pin = models.IntegerField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

class FreelancersDetails(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    pin = models.IntegerField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    skill_set = models.ManyToManyField(Skills)


