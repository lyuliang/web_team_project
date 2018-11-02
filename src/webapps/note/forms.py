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




