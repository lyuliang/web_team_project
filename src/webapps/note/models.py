import sys

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.timezone import make_aware
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
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

# def directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return '{0}/{1}'.format(instance.number, filename)

class Note(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    access_type = models.CharField(max_length=20, blank=True, default='public')
    # file = models.FileField(upload_to=directory_path, blank=False, null=False)
    file = models.FileField(upload_to='notes/', blank=False, null=False,default = '')
    filename = models.CharField(max_length=300, default='file1')

    def __str__(self):
        return self.content +"\n" + self.date + self.time


    #datetime field


class TextNote(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default = '')
    author = models.ForeignKey(User,on_delete=models.CASCADE, default = '')
    filepath=models.CharField(max_length=200, default = '')
    filename=models.CharField(max_length=200, default = '')
    body = RichTextField(blank=True,default = '')
 #  body = models.CharField(max_length=sys.maxsize, blank=True, default='')
    plaintext = models.CharField(max_length=100000,blank=True, default='')
    access_type = models.CharField(max_length=20, blank=True, default='private')

    def __str__(self):
        return self.filename
