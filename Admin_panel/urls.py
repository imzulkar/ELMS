from django.urls import path
from . import views
from Students_app.views import studentRegistration

app_name = 'Admin_panel'

urlpatterns = [
    path('addcourse/', views.AddCourseView.as_view(), name='add_course'),
    path('updatecourse/<pk>', views.UpdateCourseView.as_view(), name='update_course'),
    path('courselist/', views.SubjectListView.as_view(), name='course_list'),
    path('deletecourse/<pk>', views.DeleteCourseView.as_view(), name='delete_course'),
    path('teacherlist/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacherdetails/<pk>', views.TeacherDetailView.as_view(), name='teacher_details'),
    path('addteacher/', views.AddNewTeacherView, name='add_teacher'),
    path('addstudent/', studentRegistration, name='add_student'),
    path('login/', views.AdminAuthentication, name='admin_authentication'),
    path('logout/', views.Admin_logOut, name='logout'),
    path('', views.AdminDashboard, name='admin_dashboard'),

]
