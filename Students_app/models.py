from django.db import models
from django.contrib.auth.models import User
from Teachers_app.models import TeachersList
from Admin_panel.models import Course, Semester, BatchInfo
from django.shortcuts import reverse
from django_resized import ResizedImageField


# Create your models here.

def image_file_name(instance, filename):
    return '/'.join(['images', instance.userId.first_name, filename])


class StudentsInfo(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE, related_name='students_info')
    batchId = models.ForeignKey(BatchInfo, on_delete=models.CASCADE, related_name='batch_info', default=1)
    studentID = models.IntegerField()
    student = models.BooleanField(default=True)
    father_name = models.CharField(max_length=40, blank=True)
    mother_name = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    religion = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=20, blank=True)
    nationalId = models.IntegerField(blank=True, null=True)
    profile_pic = ResizedImageField(upload_to=image_file_name, blank=True, help_text='Size Recommended: 512x512',
                                    size=[512, 512], quality=100, force_format='JPEG')

    def __str__(self):
        return str(self.studentID)


class MarksDistribution(models.Model):
    student = models.ForeignKey(StudentsInfo, on_delete=models.CASCADE)
    quiz_1 = models.IntegerField(default=0)
    quiz_2 = models.IntegerField(default=0)
    quiz_3 = models.IntegerField(default=0)
    Assignment = models.IntegerField(default=0)
    presentation = models.IntegerField(default=0)
    mid = models.IntegerField(default=0)
    final = models.IntegerField(default=0)
    mid_improvement = models.IntegerField(default=0)

    def __str__(self):
        avg = str((self.quiz_1 + self.quiz_2 + self.quiz_3) / 3)
        sid = str(self.student)
        return 'Quid Avg:' + avg + '----ID:' + sid

    def get_absolute_url(self):
        return reverse('Teachers_app:student_list')


class RegisteredCourse(models.Model):
    student = models.ForeignKey(StudentsInfo, on_delete=models.CASCADE, related_name='abc')
    registeredCourse = models.ForeignKey(Course, on_delete=models.CASCADE)
    registeredSemester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    # info = str(student) + ' '+ str(registeredCourse)+ ' '+str(registeredSemester)
    def __str__(self):
        template = '{0.student}, {0.registeredCourse}, {0.registeredSemester}'
        return template.format(self)


class StudentFeedbackModel(models.Model):
    student = models.CharField(max_length=70, default='Anonymous')
    header = models.CharField(max_length=200)
    feedback = models.CharField(max_length=500)

    def __str__(self):
        return self.header


reasons = (
    ('td', 'Temporary Drop'),
    ('pt', 'Program Transfer'),
    ('pd', 'Permanent Drop'),
    ('ir', 'Internship Running'),
)


class DropSemesterModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='drop_semester_user', verbose_name='User')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='semester_drop_semester',
                                 verbose_name='Semester')
    semDropCause = models.CharField(choices=reasons, max_length=100, verbose_name='Semester Drop Cause')
    dropReason = models.TextField(verbose_name='Drop Reasons')
    dropDate = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.semester}'


class ApplicationTypeModel(models.Model):
    applicationType = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.applicationType}'


class StudentApplicationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_application_user')
    applicationType = models.ForeignKey(ApplicationTypeModel, on_delete=models.CASCADE, related_name='application_type')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='student_application_semester')
    instruction = models.CharField(max_length=255, blank=True)
    applicationBody = models.TextField()
    applicationTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.applicationType}'
