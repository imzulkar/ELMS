from django.contrib import admin
from .models import TeachersDepartment,TeachersFaculty,TeachersList,TeachersDesignation
# Register your models here.
admin.site.register(TeachersList)
admin.site.register(TeachersDepartment)
admin.site.register(TeachersFaculty)
admin.site.register(TeachersDesignation)

