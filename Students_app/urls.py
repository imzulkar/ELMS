from django.urls import path
from Students_app import views

app_name = 'Students_app'
urlpatterns =[
    path('',views.indexView,name='index'),
    # path('student_registration/',views.studentRegistration,name='student_registration'),
    path('studentportal/',views.studenDashboard,name='studentdashboard'),
    path('login/',views.userAuthentication,name='login'),
    path('userauthentication/',views.userAuthentication,name='userauthentication'),
    path('logout/',views.userLogout,name='logout'),
    path('course_register/',views.CourseRegistration,name='course_register'),
    path('profile/',views.StudentProfile,name='student_profile'),
    path('updateprofile/',views.StudentProfileUpdate,name='StudentProfileUpdate'),
    path('livechat/',views.main_view,name='chat'),



]