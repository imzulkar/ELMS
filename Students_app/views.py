from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from Students_app.models import StudentsInfo, RegisteredCourse, MarksDistribution, DropSemesterModel, \
    StudentApplicationModel
from Teachers_app.models import TeachersList
from chat_app.views import main_view
from django.contrib import messages
from Students_app import forms
from Students_app.forms import StudentForm, StudentLinkForm, loginForm, CourseRegistrationForm, updateStudentProfile, \
    MarkDistributionForm


# Create your views here.

def studentRegistration(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        form2 = StudentLinkForm(data=request.POST)

        if form.is_valid() and form2.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            user_info = form2.save(commit=False)
            user_info.userId = user
            user_info.save()

    else:
        form = StudentForm()
        form2 = StudentLinkForm()

    return render(request, 'Admin_panel/add_teacher.html', context={'form': form, 'form2': form2})


def indexView(request):
    current_user = request.user
    user_id = current_user.id
    try:
        user_info = TeachersList.objects.get(userId__pk=user_id)
        if user_info.teacher:
            return HttpResponseRedirect(reverse('Teachers_app:teachers_dashboard'))


    except:
        return render(request, 'Students_app/index.html', context={})


@login_required(login_url='Students_app:login')
def studenDashboard(request):
    current_user = request.user
    user_id = current_user.id
    user_info = User.objects.get(pk=user_id)
    user_more_info = StudentsInfo.objects.get(userId__pk=user_id)

    return render(request, 'Students_app/student_Dashboard.html',
                  context={'user_info': user_info, 'user_more_info': user_more_info})


@login_required(login_url='Students_app:login')
def StudentProfile(request):
    current_user = request.user
    user_id = current_user.id
    user_info = User.objects.get(pk=user_id)
    user_more_info = StudentsInfo.objects.get(userId__pk=user_id)
    return render(request, 'Students_app/student_profile.html',
                  context={'user_info': user_info, 'user_more_info': user_more_info})


@login_required(login_url='Students_app:login')
def StudentProfileUpdate(request):
    studentId = request.user.id
    studentInfo = StudentsInfo.objects.get(userId__pk=studentId)
    form = updateStudentProfile(instance=studentInfo)

    if request.method == 'POST':
        form = updateStudentProfile(request.POST, request.FILES, instance=studentInfo)
        if form.is_valid():
            form.save()

    return render(request, 'Students_app/update_profile.html', context={'form': form})


def userAuthentication(request):
    form = loginForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # print(username, password)

            user = authenticate(username=username, password=password)

            if user is not None:
                print(user, user.id)
                try:
                    user_id = user.id
                    verify = StudentsInfo.objects.get(userId__pk=user_id)
                    if verify.student:
                        login(request, user)
                        return HttpResponseRedirect(reverse('Students_app:studentdashboard'))
                except:
                    print('you are not Student')
                    return redirect('Students_app:login')

    return render(request, 'Students_app/login.html', context={'form': form})


@login_required(login_url='Students_app:login')
def passwordChangeView(request):
    form = forms.PasswordChangeForm()

    if request.method == 'POST':
        form = forms.PasswordChangeForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            print(password2)
            print(password)
            if password == password2:
                user = User.objects.get(username=request.user.username)
                user.set_password(password)
                user.save()
                return HttpResponseRedirect(reverse('Students_app:studentdashboard'))

    return render(request, 'Students_app/passwordChange.html', context={'form': form})


# @login_required(login_url='Students_app:login')
def CourseRegistration(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(data=request.POST)
        current_user = request.user
        user_id = current_user.id
        user_info = StudentsInfo.objects.get(userId__pk=user_id)
        student_info = form.save(commit=False)
        student_info.student = user_info
        # Twice course registration check
        student_info.save()
    else:
        form = CourseRegistrationForm()

    diction = {'form': form}
    return render(request, 'Students_app/test.html', context=diction)


@login_required(login_url='Students_app:login')
def dropSemesterView(request):
    form = forms.DropSemesterForm()
    dropSemesterDetail = DropSemesterModel.objects.filter(user=request.user)
    if request.method == 'POST':
        form = forms.DropSemesterForm(data=request.POST)
        if form.is_valid():
            dropInfo = form.save(commit=False)
            dropInfo.user = request.user
            dropInfo.save()
            return HttpResponseRedirect(reverse('Students_app:drop_semester'))
    return render(request, 'Students_app/dropSemester.html',
                  context={'form': form, 'dropSemDetails': dropSemesterDetail})


@login_required(login_url='Students_app:login')
def routineView(request):
    return render(request, 'Students_app/routine.html', context={})


@login_required(login_url='Students_app:login')
def studentApplicationView(request):
    form = forms.StudentApplicationForm()
    myApplication = StudentApplicationModel.objects.filter(user=request.user)

    if request.method == 'POST':
        form = forms.StudentApplicationForm(data=request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()

            return HttpResponseRedirect(reverse('Students_app:student_application_view'))
    return render(request, 'Students_app/student_application.html',
                  context={'form': form, 'myApplication': myApplication})


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Students_app:login'))
