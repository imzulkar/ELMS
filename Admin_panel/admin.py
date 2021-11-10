from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Semester)
admin.site.register(models.OfferedCourse)
admin.site.register(models.BatchInfo)