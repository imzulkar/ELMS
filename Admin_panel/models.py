from django.db import models
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from Teachers_app.models import TeachersList
# Create your models here.



class Course(models.Model):
    courseCode = models.CharField(max_length=10,default='')
    courseTitle = models.CharField(max_length=40,default='')
    courseCredit = models.IntegerField()

    def __str__(self):
        return self.courseCode

    def get_absolute_url(self):
        return reverse('Admin_panel:add_course')

class Semester(models.Model):
    semester = models.CharField(max_length=30,default='')
    def __str__(self):
        return self.semester


# Graduation on BBA/MBA/Engineering/English
class OfferedCourse(models.Model):
    courseName = models.CharField(max_length=30)
    courseCredit = models.IntegerField()
    courseGraduationYear = models.IntegerField()
    courseCost = models.IntegerField()

    def __str__(self):
        return self.courseName + "Cost: "+ str(self.courseCost)



class BatchInfo(models.Model):
    batch = models.IntegerField(null=True,default=1)
    section = models.CharField(max_length=4, null=True,default='A')
    assignTeacher = models.ForeignKey(TeachersList,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.batch) + '-'+self.section


#
# class StudentsInfoModel(models.Model):
#     userId = models.OneToOneField(User, on_delete=models.CASCADE)
#     studentID = models.IntegerField()
#     student = models.BooleanField(default=True)
#     father_name = models.CharField(max_length=40,blank=True)
#     mother_name = models.CharField(max_length=40,blank=True)
#     address = models.CharField(max_length=100,blank=True)
#     phone = models.IntegerField(blank=True,null=True)
#     dateOfBirth = models.DateField(blank=True,null=True)
#     gender = models.CharField(max_length=10,blank=True)
#     religion = models.CharField(max_length=20,blank=True)
#     nationality = models.CharField(max_length=20,blank=True)
#     nationalId = models.IntegerField(blank=True,null=True)
#
#     def __str__(self):
#         return str(self.studentID)