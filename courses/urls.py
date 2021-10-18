from . import views
from django.urls import path , include


urlpatterns = [
    path('', views.course_info, name = 'CourseHome'),
    path('create/',views.create, name = 'CourseCreate'),
    path('join/',views.join,name = 'CourseJoin'),
    path('<int:course_id>/',views.course,name = 'coursepage'),
]