from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from Students_app.models import StudentsInfo,RegisteredCourse,MarksDistribution
from Teachers_app.models import TeachersList
from chat_app.views import main_view
from django.contrib import messages
from Students_app import forms
from Students_app.forms import StudentForm,StudentLinkForm,loginForm,CourseRegistrationForm,updateStudentProfile,MarkDistributionForm
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



    return render(request,'Admin_panel/add_teacher.html',context={'form':form,'form2':form2})
def indexView(request):
    current_user = request.user
    user_id = current_user.id
    try:
        user_info = TeachersList.objects.get(userId__pk=user_id)
        if user_info.teacher:
            return HttpResponseRedirect(reverse('Teachers_app:teachers_dashboard'))


    except:
        return render(request,'Students_app/index.html',context={})


@login_required(login_url='Students_app:login')
def studenDashboard(request):
    current_user = request.user
    user_id = current_user.id
    user_info = User.objects.get(pk=user_id)
    user_more_info = StudentsInfo.objects.get(userId__pk=user_id)

    return render(request,'Students_app/student_Dashboard.html',context={'user_info':user_info, 'user_more_info':user_more_info})

@login_required(login_url='Students_app:login')
def StudentProfile(request):
    current_user = request.user
    user_id = current_user.id
    user_info = User.objects.get(pk=user_id)
    user_more_info = StudentsInfo.objects.get(userId__pk=user_id)
    return render(request, 'Students_app/student_profile.html',
                  context={'user_info': user_info, 'user_more_info': user_more_info})


def StudentProfileUpdate(request):
    studentId = request.user.id
    studentInfo = StudentsInfo.objects.get(userId__pk=studentId)
    form = updateStudentProfile(instance=studentInfo)

    if request.method == 'POST':
        form =updateStudentProfile(request.POST,instance=studentInfo)

        if form.is_valid():
            form.save()

    return render(request, 'Students_app/update_profile.html', context={'form': form})


def userAuthentication(request):
    form = loginForm()
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # print(username, password)

            user = authenticate(username=username,password=password)

            if user is not None:
                print(user,user.id)
                try:
                    user_id = user.id
                    verify = StudentsInfo.objects.get(userId__pk=user_id)
                    if verify.student:
                        login(request,user)
                        return HttpResponseRedirect(reverse('Students_app:studentdashboard'))
                except:
                    print('you are not Student')
                    return redirect('Students_app:login')

    return render(request,'Students_app/login.html',context={'form':form})

# @login_required(login_url='Students_app:login')
def CourseRegistration(request):
    if request.method=='POST':
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
    return render(request,'Students_app/test.html',context=diction)


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Students_app:login'))