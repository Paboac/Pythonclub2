from collections import UserString
from turtle import onclick
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
     meetingtitle=models.CharField(max_length=100)
     meetingdate=models.DateField()
     meetinglocation=models.CharField(max_length=255)
     meetingagenda=models.CharField(max_length=400)



     def __str__(self):
          return self.meetingtitle
     
     class Meta:
          db_table='Meeting'

class Meetingminutes(models.Model):
     meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
     attendance=models.ManyToManyField(User, max_length=255)
     minutestext=models.IntegerField()




     def __str__(self):
          return self.meetingid

     class Meta:
          db_table='Meetingminutes'


class Resource(models.Model):
     resourcename=models.CharField(max_length=255)
     resrourcetype=models.CharField(max_length=255)
     resourceurl=models.URLField()
     dateentered=models.DateTimeField()
     userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
     resourcedescription=models.TextField()

     def __str__(self):
          return self.resourcename

     class Meta:
          db_table='Resource'

class Event(models.Model):
     eventtitle=models.CharField(max_length=255)
     location=models.CharField(max_length=255)
     eventdate=models.DateField()
     eventtime=models.TimeField()
     eventdescription=models.TextField(max_length=400)
     userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

     def __str__(self):
          return self.eventtitle
     
     class Meta:
          db_table='Event'









