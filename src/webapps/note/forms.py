from django import forms
from note.models import *

class LogInForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100)
    pw = forms.CharField(label = 'Password', max_length=100, widget = forms.PasswordInput)
    identity = forms.CharField(label = 'Identity', max_length=10)
    # Check If Identity is consistent 
    def clean(self):
        cleaned_data = super(LogInForm, self).clean()  #Don't forget to call super.clean()
        idenity = self.cleaned_data['identity']
        if idenity != 'S' and idenity != 'P':
            raise forms.ValidationError("Illegal Identity For User!")
        if idenity == 'S':
            if Student.objects.filter(username = cleaned_data['username']).count() == 0:
                raise forms.ValidationError("Student Not Found!")
        if idenity == 'P':
            if Professor.objects.filter(username = cleaned_data['username']).count() == 0:
                raise forms.ValidationError("Professor Not Found!")
        return cleaned_data
       

class RegisterForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100)
    andrewid = forms.CharField(label = 'Andrew Id',max_length=100)
    pw = forms.CharField(label = 'Password', max_length=100, widget = forms.PasswordInput)
    pw2 = forms.CharField(label = 'Password Confirmation', max_length=100,widget = forms.PasswordInput)
    identity = forms.CharField(label = 'Identity', max_length=10)
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pw = self.cleaned_data['pw']
        pw2 = self.cleaned_data['pw2']
        if pw != pw2:
            raise forms.ValidationError("Repeated Password is different!")
        return cleaned_data

    def clean_identity(self):
        idenity = self.cleaned_data.get('identity')
        if idenity != 'S' and idenity != 'P':
            raise forms.ValidationError("Illegal Identity For User!")
         # TODO Validation
        return idenity

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        widgets = {'name': forms.Textarea(),
                   'number': forms.Textarea()}
        fields = ['name', 'number']

    def __init__(self, *args, **kwargs):
        super(CreateCourseForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Course Name',
                                                 'name':'course_name', 'id':'course_name'})
        self.fields['number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Course Number (5 digits)',
                                                 'name':'course_number', 'id':'course_number'})

    def clean_number(self):
        number = self.cleaned_data.get('number')
        print('number::', number)
        if len(number) != 5 or not number.isdigit():
            raise forms.ValidationError("Course number should be 5-digit integer")
        if Course.objects.filter(number=number):
            raise forms.ValidationError("Course number already exists.")
        return number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        print('name::', name)
        if Course.objects.filter(name=name):
            raise forms.ValidationError("Course name already exists.")
        return name
    def clean(self):
        cleaned_data = super(CreateCourseForm, self).clean()
        name = cleaned_data.get('name')
        number = cleaned_data.get('number')
        print('name::', name)
        print('number::', number)
        if not name or not number:
            raise forms.ValidationError("Must fill in course name and course number!")
        return cleaned_data

class JoinCourseForm(forms.Form):
    name = forms.CharField(max_length=300, required=False)
    number = forms.CharField(max_length=40, required=False)
    def __init__(self, *args, **kwargs):
        super(JoinCourseForm, self).__init__(*args, **kwargs)
    def clean(self):
        cleaned_data = super(JoinCourseForm, self).clean()
        name = cleaned_data.get('name')
        number = cleaned_data.get('number')
        if not name and not number:
            raise forms.ValidationError("Must fill in course name or course number!")
        return cleaned_data

    def clean_number(self):

        number = self.cleaned_data.get('number')
        if len(number) != 0 and (len(number) != 5 or not number.isdigit()):
            raise forms.ValidationError("Course number should be 5-digit integer")
        return number
    def clean_name(self):
        return self.cleaned_data.get('name')




