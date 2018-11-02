from django.db import models
from django.utils.timezone import make_aware
from django.contrib.auth.models import User
import datetime
class myUser(User):
    age = models.IntegerField(blank = True, default = 0)
    bio = models.CharField(max_length=420, blank = True, default = '')
    profile_picture = models.FileField(upload_to = "profile_photos", blank = True, default = '')
    myToken = models.CharField(max_length=100,blank = True, default = '')
    followers = models.ManyToManyField("self", blank = True)
    def __str__(self):
        return self.username 
    
class POSTING(models.Model):
    content = models.CharField(max_length=42)
    poster = models.ForeignKey(myUser,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content +"\n" + self.poster + self.date + self.time
    #datetime field
    # Get new modied time
    @staticmethod
    def get_changes(timestamp=0):
        t = make_aware(datetime.datetime.fromtimestamp(timestamp/1000.0))
        return POSTING.objects.filter(last_modified__gt=t).order_by('-date','-time').distinct()

class COMMENT(models.Model):
    content = models.CharField(max_length=42)
    author = models.ForeignKey(myUser,on_delete=models.CASCADE)
    posting = models.ForeignKey(POSTING,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.content +"\n" + self.date + self.time
    #datetime field

