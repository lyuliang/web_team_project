from django.db import models
from django.utils.timezone import make_aware
from django.contrib.auth.models import User
import datetime

class Student(User):
    andrewid = models.CharField(max_length=20, blank = True, default = '') 
    identity = models.CharField(max_length=10, blank = True, default = 'S') # 'S' for Student, P for Professor
    def __str__(self):
        return self.username 

class Professor(User):
    andrewid = models.CharField(max_length=20, blank = True, default = '') 
    identity = models.CharField(max_length=10, blank = True, default = 'P') # 'S' for Student, P for Professor
    def __str__(self):
        return self.username 
    
class Course(models.Model):
    name = models.CharField(max_length=300)
    number = models.CharField(max_length=40)
    instructor = models.ForeignKey(Professor,on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    def __str__(self):
        return self.number + self.name


class Note(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE) 
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    access_type = models.CharField(max_length=20, blank = True, default = 'public')
    def __str__(self):
        return self.content +"\n" + self.date + self.time
    #datetime field

