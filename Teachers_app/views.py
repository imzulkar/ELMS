from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TeachersListForm, loginForm, RegisteredCourseForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from Teachers_app.models import TeachersList, TeachersFaculty, TeachersDepartment, TeachersDesignation
from Students_app.forms import StudentForm, StudentLinkForm, MarkDistributionForm
from Students_app.models import MarksDistribution, StudentsInfo, RegisteredCourse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView, ListView, DetailView


# Create your views here.
# @login_required(login_url='Teachers_app:teacherslogin')
def index(request):
    form = TeachersListForm()
    diction = {'form': form}
    return render(request, 'Teachers_app/teachers_base.html', context=diction)


def TeacherAuthentication(request):
    form = loginForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # print(username, password)

            user = authenticate(username=username, password=password)

            if user is not None:
                # print(user,user.id)
                try:
                    user_id = user.id
                    verify = TeachersList.objects.get(userId__pk=user_id)
                    if verify.teacher:
                        login(request, user)
                        return HttpResponseRedirect(reverse('Teachers_app:teachers_dashboard'))
                except:
                    print('you are not Teacher')
                    return redirect('Teachers_app:teacherslogin')

    return render(request, 'Teachers_app/login.html', context={'form': form})


# Teachers dashboard
@login_required(login_url='Teachers_app:teacherslogin')
def TeachersDashboard(request):
    current_user = request.user
    user_id = current_user.id
    user_info = TeachersList.objects.get(userId__pk=user_id)
    diction = {'title': 'Dashboard', 'user_info': user_info}
    return render(request, 'Teachers_app/teachers_dashboard.html', context=diction)


# Teacher profile page
@login_required(login_url='Teachers_app:teacherslogin')
def TeachersProfile(request):
    current_user = request.user
    user_id = current_user.id
    teachers_info = User.objects.get(pk=user_id)
    teachers_details = TeachersList.objects.get(userId__pk=user_id)
    diction = {'teachers_info': teachers_info, 'teachers_details': teachers_details, 'title': 'profile'}
    return render(request, 'Teachers_app/teachers_profile.html', context=diction)


@login_required(login_url='Teachers_app:teacherslogin')
def NewStudentRegistration(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        form2 = StudentLinkForm(data=request.POST)
        autoGenerate = MarkDistributionForm()
        if form.is_valid() and form2.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            user_info = form2.save(commit=False)
            user_info.userId = user
            user_info.save()
            autoGenerate.is_valid()

            print(user_info)
            MarksDistribution.objects.create(student=user_info)
            # autoGenerate.student = user_info
            # print(autoGenerate.student)
            # autoGenerate.save()
    else:
        form = StudentForm()
        form2 = StudentLinkForm()

    return render(request, 'Teachers_app/newstudent_registration.html', context={'form': form, 'form2': form2})


@login_required(login_url='Teachers_app:teacherslogin')
def TeacherLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Teachers_app:teacherslogin'))


# Marks
class Students_list(ListView):
    model = User
    context_object_name = 'students'
    queryset = User.objects.filter(students_info__student=True)
    template_name = 'Teachers_app/students_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)


class AddMarks(UpdateView):
    model = MarksDistribution
    fields = ['quiz_1', 'quiz_2', 'quiz_3', 'Assignment', 'presentation', 'mid', 'final', 'mid_improvement']
    context_object_name = 'marks'
    template_name = 'Teachers_app/marks_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

#
# def CourseInstructor(request):
