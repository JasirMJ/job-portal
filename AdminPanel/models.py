from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Images(models.Model):
    # name = models.ImageField()
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=10)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.file.name

class Categories(models.Model):
    name = models.CharField(max_length=15)

class Skills(models.Model):
    name = models.CharField(max_length=20)
    category = models.ManyToManyField(Categories)

class UserDetails(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    firebase = models.CharField(max_length=50)
    mobile = models.IntegerField()
    pin = models.IntegerField( null=True)
    latitude = models.CharField(max_length=50,null=True)
    longitude = models.CharField(max_length=50,null=True)
    profile_pic = models.ManyToManyField(Images,null=True)
    skill = models.ManyToManyField(Skills,null=True)
    is_freelancer = models.IntegerField()



