from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from Students_app.forms import DateInput
from .models import TeachersList, UpdateNotice
from Students_app.models import RegisteredCourse,MarksDistribution


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
        fields = '__all__'


class updateTeacherProfile(ModelForm):
    class Meta:
        model = TeachersList
        exclude = ('userId', 'empid', 'teacher')


class PasswordChangeForm(ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('password', 'password2')
        widgets = {
            'password': forms.PasswordInput,

        }


class MarkDistributionForm(ModelForm):
    class Meta:
        model = MarksDistribution
        exclude = ('student',)


class UpdatePostForm(ModelForm):
    class Meta:
        model = UpdateNotice
        exclude = ('postedBy',)
