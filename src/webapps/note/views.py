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
        identity = form.cleaned_data['identity']
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['pw'])
        if(not user):
            errors.append('Anthentication Error!')
            print('log failure')
            context['errors'] = errors
            return render(request, 'login.html', context)
        login(request,user)
        # Redirect to Index page
        print('login success')
        # return index(request)

        return redirect(reverse('index', args=(identity)))
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
    return redirect(reverse('index', args=(identity)))

# Log out, return to Log in home page
@login_required
def logOut(request):
    errors = []
    context = {}
    context['errors'] = errors
    logout(request)
    return render(request, 'login.html', context)

@login_required
def index(request, identity):
    context = {}
    context['identity'] = identity
    if identity == 'S':
        if request.method == 'GET':
            print('JoinCourseForm()')
            context['form'] = JoinCourseForm()
            student = Student.objects.get(username = request.user.username)
            # Find courses took the logged in student
            courses = student.course_set.all()
            if len(courses):
                context['courses'] = courses
            else:
                context['courses'] = Course.objects.all()
        return render(request, 'index_student.html', context)
    else:
        if request.method == 'GET':
            print('CreateCourseForm()')
            context['form'] = CreateCourseForm()
            prof = Professor.objects.get(username = request.user.username)
            # Find courses taught by the logged in professor
            courses = Course.objects.filter(instructor = prof)
            if len(courses):
                context['courses'] = courses
            else:
                context['courses'] = Course.objects.all()
            print(courses)
        return render(request, 'index_prof.html', context)

@login_required
def course(request,course_id, identity):
    context = {}
    context['identity'] = identity 
    return render(request,'course.html',context)

@login_required
@transaction.atomic
def create_course(request):
    print('enter create course')
    instructor = get_object_or_404(Professor, username=request.user.username)
    print('instructor name:',instructor.username)
    new_course = Course(instructor=instructor)
    # new_course.name = request.POST.get('name')
    # new_course.number = request.POST.get('number')
    print(request.POST)
    # print(new_course.name)
    # print(new_course.number)
    form = CreateCourseForm(request.POST, instance=new_course)
    if not form.is_valid():
        # raise Http404
        print('error:', form.errors)
        return HttpResponse(form.errors)
    else:
        print('no error')
        form.save()
    return HttpResponse("")

@login_required
@transaction.atomic
def join_course(request):
    student = get_object_or_404(Student, username=request.user.username)
    form = JoinCourseForm(request.POST)
    if not form.is_valid():
        print('error:', form.errors)
        return HttpResponse(form.errors)
    name = form.cleaned_data['name']
    number = form.cleaned_data['number']
    course1 = Course.objects.filter(name=name)
    course2 = Course.objects.filter(number=number)
    print('course1:',course1, ' course2:',course2)
    if not course1 and not course2:
        print(("Course Not Found!"))
        return HttpResponse("Course Not Found!")
    elif not course2:
        course = course1[0]
    elif not course1:
        course = course2[0]
    elif course1[0] != course2[0]:
        print("Course name and number don't match!")
        return HttpResponse("Course name and number don't match!")
    else:
        course = course1[0]

    if student in course.students.all():
        print("Already joined this course!")
        return HttpResponse("Already joined this course!")

    course.students.add(student)
    course.save()
    print(course.students)
    return HttpResponse("")


