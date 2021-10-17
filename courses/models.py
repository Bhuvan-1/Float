from django.db import models

# Create your models here.

from django.contrib.auth.models import  User
from django.db.models.fields import DateTimeField
from django.db.models.signals import post_save
import requests



# class Course(models.Model):

#     instructor = models.ForeignKey(User,on_delete=models.CASCADE)

#     name = models.CharField(max_length=128,default = '')
#     star_count = models.IntegerField(default=0)
#     #Assignments
#     #Lectures
#     #Grades


#     def __str__(self):
#             return self.name

# class Student(models.Model):

#     user = models.OneToOneField(User,on_delete=models.CASCADE)

#class Instructor

#class Assignment

'''when a course is created by instructor then a Instrucctor model instance si created. When a student
is added to  acourse then a Student model is created and they are linked to each other and also 
to th ecourse model'''

'''USE SIGNALS'''
#add app to the list. and migrations admin.py etc...

