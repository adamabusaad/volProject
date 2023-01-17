from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import BooleanField, ChoiceField, Select


# Create your models here
#
CITY_OPTIONS = (
    ('BEERSHEVA', 'Beer Sheva'),
    ('TELAVIV', 'Tel Aviv'),
    ('ASHDOD', 'Ashdod'),
    ('HAIFA', 'HAIFA'),
    ('RHOVOT', 'Rhovot'),
    ('JERUSALEM', 'Jerusalem'),

)

class User(AbstractUser):

    ADMIN = 1
    STUDENT = 2
    SACERTARY = 3


    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STUDENT, 'Student'),
        (SACERTARY, 'Sacertary'),

    )
    role = models.PositiveSmallIntegerField(default= STUDENT,choices=ROLE_CHOICES, blank=True)
    city = models.CharField(max_length=20, choices=CITY_OPTIONS, default=None, blank=True, null=True)



class ScheduleModel(models.Model):
    Reciever = models.ForeignKey(User,on_delete=models.CASCADE)
    username= models.CharField(max_length=250,blank=True,null=True)
    subject=models.CharField(max_length=250,blank=True,null=True)
    message = models.TextField(max_length=250,blank=True,null=True)
