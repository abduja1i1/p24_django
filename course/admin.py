from django.contrib import admin

from course.models import Teacher, Speciality, Subject, StudentInfo, Student

admin.site.register([Teacher, Speciality, Subject, StudentInfo, Student])
