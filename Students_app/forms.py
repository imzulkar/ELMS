from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Students_app.models import StudentsInfo,RegisteredCourse,MarksDistribution



class MarkDistributionForm(ModelForm):
    class Meta:
        model = MarksDistribution
        fields = ('student',)

class StudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        help_texts = {
            'username': None,
            'password2':None,
        }
class StudentLinkForm(ModelForm):
    class Meta:
        model = StudentsInfo
        fields= ('studentID','batchId')

class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        # kwargs["format"] = "%Y-%m-%d"
        kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class updateStudentProfile(ModelForm):
    class Meta:
        model= StudentsInfo
        exclude = ('userId', 'studentID','student',)
        widgets ={
            'dateOfBirth':DateInput(format=["%d-%m-%Y"],),
        }


class loginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)



class CourseRegistrationForm(ModelForm):
    class Meta:
        model =RegisteredCourse
        fields = ('registeredSemester','registeredCourse',)






