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

def logIn(request):
    errors = []
    context = {}
    context['errors'] = errors
    if request.method == "GET":
        return render(request, 'login.html', context)
    # Login POST Request
    form = LogInForm(request.POST)
    context['form'] = form
    if 'identity' not in request.POST:
        context['errors'] = ['Choose Your Identity']
        return render(request, 'login.html', context)
    elif form.is_valid():
        identity = form.cleaned_data['identity']
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['pw'])
        if(not user):
            errors.append('Wrong Password')
            context['errors'] = errors
            return render(request, 'login.html', context)
        # Login Success
        login(request,user)
        # Redirect to Index page
        print('login success')
        return redirect(reverse('index', args=(identity)))
    else: # Form Error
        for e in form.non_field_errors():
            context['errors'].append(e)
        for field in form.visible_fields():
            for e in field.errors:
                context['errors'].append(e)
        return render(request, 'login.html', context)
        # error

def register(request):
    errors = []
    context = {}
    context['errors'] = errors
    if request.method=='GET':
        return render(request,"register.html",context)

    form = RegisterForm(request.POST)
    # Error happens, Refreshing Signup Page
    if not form.is_valid():
        for e in form.non_field_errors():
            context['errors'].append(e)
        for field in form.visible_fields():
            for e in field.errors:
                context['errors'].append(e)
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
    course = Course.objects.get(id=course_id)
    notes = Note.objects.filter(course = course)
    context['course_number'] = course.number
    context['course_name'] = course.name
    context['notes'] = notes
    return render(request,'course.html',context)

@login_required
@transaction.atomic
def create_course(request):
    print('enter create course')
    instructor = get_object_or_404(Professor, username=request.user.username)
    # Find if the prof has created some courses
    courses = Course.objects.filter(instructor = instructor)
    unselected = False
    # Hasn't selected courses yet
    if len(courses):
         unselected = True
    #Create A new Course
    new_course = Course(instructor=instructor)
    form = CreateCourseForm(request.POST, instance=new_course)
    if not form.is_valid():
        # raise Http404
        errors = []
        for error in form.non_field_errors():
            errors.append(error)
        for field in form.visible_fields():
            errors.append(field.errors)
        print('error:', form.errors)
        return render(request,'errors.html', context = {'errors':errors})
    else:
        print('no error')
        form.save()
    return render(request,'single-course.html',
        context = {'course':new_course, 'identity':'P','unselected':unselected})

@login_required
@transaction.atomic
def join_course(request):
    student = get_object_or_404(Student, username=request.user.username)
    form = JoinCourseForm(request.POST)

    courses = student.course_set.all()
    unselected = False
    # Hasn't selected courses yet
    if len(courses):
         unselected = True
    if not form.is_valid():
        errors = []
        for error in form.non_field_errors():
            errors.append(error)
        for field in form.visible_fields():
            errors.append(field.errors)
        print('error:', form.errors)
        return render(request, 'errors.html', context={'errors': errors})

    name = form.cleaned_data['name']
    number = form.cleaned_data['number']
    course1 = Course.objects.filter(name=name)
    course2 = Course.objects.filter(number=number)
    print('course1:',course1, ' course2:',course2)
    if not course1 and not course2:
        print(("Course Not Found!"))
        return HttpResponse("Error: Course Not Found!")
    elif not course2:
        course = course1[0]
    elif not course1:
        course = course2[0]
    elif course1[0] != course2[0]:
        print("Course name and number don't match!")
        return HttpResponse("Error: Course name and number don't match!")
    else:
        course = course1[0]

    if student in course.students.all():
        print("Already joined this course!")
        return HttpResponse("Error: Already joined this course!")

    course.students.add(student)
    course.save()
    print(course.students)
    return render(request,'single-course.html', \
            context = {'course':course, 'identity':'S','unselected':unselected})
@login_required
@transaction.atomic
def upload_file(request):
    if request.method == 'POST':
        print(request.POST)
        uploaded_file = request.FILES.get('input_file')
        print(type(uploaded_file))
        print(uploaded_file._get_name())
        # form = NoteForm(request.FILES)
        if not uploaded_file:
            return HttpResponse('Must choose a file!')

        print('course# current', request.POST.get('course_number'))
        course = Course.objects.get(number=request.POST.get('course_number'))
        new_note = Note(author=request.user, course=course, date=datetime.date, time=datetime.time)
        new_note.filename = uploaded_file._get_name()
        new_note.save()
        new_note.file.save(uploaded_file._get_name(), uploaded_file)

        return render(request,'single-note.html', context = {'note':new_note, 'identity':'S'})

    return render(request,'course.html',{})

@login_required
@transaction.atomic
def create_note(request):
    context = {}
    if request.method=='GET':
        # context['identity'] = identity
        # course = Course.objects.get(id=course_id)
        # context['course_number'] = course.number
        # context['course_name'] = course.name
        return render(request, 'create_note.html', context)