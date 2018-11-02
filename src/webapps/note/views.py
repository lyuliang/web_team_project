from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout,tokens
from django.contrib.auth.decorators import login_required
from note.models import *
from note.forms import *
from mimetypes import guess_type
from django.core.mail import send_mail
from django.db import transaction
import time
current_milli_time = lambda: int(round(time.time() * 1000))
# Create your views here.

def login(request):
    errors = []
    context = {}
    context['errors'] = errors
    
    if request.method == "GET":
        return render(request, 'login.html', context)
    