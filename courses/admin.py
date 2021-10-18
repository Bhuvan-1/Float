from django.contrib import admin

from courses.models import Course #, Instructor, Student

# Register your models here.

admin.site.register(Course)


#admin.site.register(Student)
#admin.site.register(Instructor)