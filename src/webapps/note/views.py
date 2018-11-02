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

def logIn(request):
    errors = []
    context = {}
    context['errors'] = errors
    if request.method == "GET":
        return render(request, 'login.html', context)
    # Login POST Request
    form = LogInForm(request.POST)
    context['form'] = form
    if form.is_valid():
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['pw'])
        if(not user):
            errors.append('Anthentication Error!')
            print('log failure')
            context['errors'] = errors
            return render(request, 'login.html', context)
        login(request,user)
        # Redirect to Index page
        print('login success')
        return index(request)
    else: # Form Error
        print('Form error')
        print(form.non_field_errors)
        context['errors'] = ['form_error']
        return render(request, 'login.html', context)
        # error

def register(request):
    errors = []
    context = {}
    context['errors'] = errors
    form = RegisterForm(request.POST)
    # Error happens, Refreshing Signup Page
    if not form.is_valid():
        print('-----')
        context['form'] = form
        print(form.errors)
        context['errors'] = ['form_error']
        return render(request, 'login.html', context) 
    # Create a new user according to identity

    identity = form.cleaned_data['identity']
    if identity == 'S':
        new_user = Student.objects.create_user(username = form.cleaned_data['username'],\
                                                password = form.cleaned_data['pw'])
    if identity == 'P':
        new_user = Professor.objects.create_user(username = form.cleaned_data['username'],\
                                                password = form.cleaned_data['pw'])
    #Save new User to Student/Prof Database                                           
    new_user.andrewid = form.cleaned_data['andrewid']
    print(new_user)
    new_user.save()
    #login
    new_user = authenticate(username = request.POST['username'],\
        password = request.POST['pw'])
    login(request,new_user)
    # redirect to Main page
    return index(request)

@login_required
def index(request):
    context = {}
    return render(request,'index.html',context);