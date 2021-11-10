from django.contrib import admin
from .models import MarksDistribution,RegisteredCourse,StudentsInfo
# Register your models here.
admin.site.register(MarksDistribution)
admin.site.register(StudentsInfo)
admin.site.register(RegisteredCourse)