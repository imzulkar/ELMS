# Generated by Django 3.2.11 on 2022-01-21 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachersDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TeachersDesignation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TeachersFaculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TeachersList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.BooleanField(default=True)),
                ('empid', models.IntegerField()),
                ('personalWebPage', models.URLField(default='', null=True)),
                ('phone', models.IntegerField(null=True)),
                ('department', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Teachers_app.teachersdepartment')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teachers_app.teachersdesignation')),
                ('faculty', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Teachers_app.teachersfaculty')),
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teachers_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
