from django.contrib import admin
from .models import MarksDistribution, RegisteredCourse, StudentsInfo, DropSemesterModel, ApplicationTypeModel, StudentApplicationModel,StudentFeedbackModel

# Register your models here.
admin.site.register(MarksDistribution)
admin.site.register(StudentsInfo)
admin.site.register(RegisteredCourse)
admin.site.register(DropSemesterModel)
admin.site.register(StudentFeedbackModel)
admin.site.register(ApplicationTypeModel)
admin.site.register(StudentApplicationModel)
