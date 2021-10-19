from django.contrib import admin

from courses.models import Assignment, Course, FileSubmission #, Instructor, Student

# Register your models here.

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(FileSubmission)


#admin.site.register(Student)
#admin.site.register(Instructor)