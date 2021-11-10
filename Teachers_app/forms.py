from django.forms import ModelForm
from django import forms
from .models import TeachersList
from Students_app.models import RegisteredCourse

class TeachersListForm(ModelForm):
    class Meta:
        model = TeachersList
        fields = '__all__'

class loginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisteredCourseForm(ModelForm):
    class Meta:
        model = RegisteredCourse
        fields ='__all__'