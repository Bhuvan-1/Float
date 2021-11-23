from django.db import models

# Create your models here.

from django.contrib.auth.models import  User
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.signals import post_save

import random


class Course(models.Model):

    instructor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ins_courses') #assuming 1 instructor/course.
    name = models.CharField(max_length=128,default = '')
    students = models.ManyToManyField(User,related_name='stud_courses')
    joincode = models.CharField(max_length=10,default = '')

    def __str__(self):
        return self.name

class Assignment(models.Model):
    name = models.CharField(max_length=128,default='')
    link = models.URLField(default='')
    file_name = models.CharField(max_length=100,default='problem_statement')
    file = models.FileField(upload_to='assignments',blank=True)
    statement = models.CharField(max_length=300,default='')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    maxmarks = models.IntegerField(default=100)
    deadline = models.DateTimeField(blank=False) #need to set while creating assign.

    def __str__(self):
        return self.name

class FileSubmission(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions',blank=True)
    file_name = models.CharField(max_length=100,default='submission')
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500,default='Your Feedback Appears Here')
    corrected = models.CharField(max_length=10,default='NO')
    grade = models.IntegerField(default=-1)
    sub_time = models.DateTimeField(auto_now=True) #last 'MODIFIED' time. // automatically updates itself.


    def __str__(self):
        return self.user.username + self.file_name + self.assignment.name



# class Instructor(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

# class Student(models.Model):

#     user = models.OneToOneField(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

'''when a course is created by instructor then a Instrucctor model instance si created. When a student
is added to  acourse then a Student model is created and they are linked to each other and also 
to th ecourse model'''

'''USE SIGNALS'''
#add app to the list. and migrations admin.py etc...

