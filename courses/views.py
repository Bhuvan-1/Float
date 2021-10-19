from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.db.models.signals import post_save
from django.contrib.auth.models import User

import courses
from .forms import AssignCreationForm, AssignmentSubmitForm, CourseCreationForm , CourseJoinForm
from .models import Assignment, Course, FileSubmission #, Student , Instructor
import random
# Create your views here.



def generate_code(): #function to generate random course code.
    s = ""
    for i in range(0,6):
        c = random.randint(65,90)
        s += chr(c)
    return s

'''--------------------------------------------------------------'''

def course_info(request):

    if not request.user.is_authenticated:
        return redirect('login')

    u = User.objects.get(pk = request.user.pk )
    args = {
        'icourses': u.stud_courses.all(),
        'scourses': u.ins_courses.all(),
    }

    return render(request,'courses/home.html',args)

def create(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            course_name = form.cleaned_data['name']
            code = generate_code()

            e = Course.objects.all().filter(joincode = code).count()
            while e != 0:
                code = generate_code()
                e = Course.objects.all().filter(joincode = code).count()

            e = Course.objects.all().filter(name = course_name).count()
            if( e != 0): #Name already exists.
                args = {'form': form, 'wrong': True}
                return render(request, 'courses/create.html', args)

            c = Course.objects.create(instructor = request.user)
            c.name = course_name
            c.joincode = code
            c.save()

            return redirect('CourseHome')

    else:
        form = CourseCreationForm()

    return render(request, 'courses/create.html', {'form': form, 'wrong': False})
'---------------------------------------------------------------------------'

def join(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CourseJoinForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            code = form.cleaned_data['code']
            e = Course.objects.all().filter(joincode = code).count()

            if( e == 0):  #incorrect course code.
                args = {'form': form, 'wrong': True}
                return render(request, 'courses/join.html', args)
            
            c = Course.objects.get(joincode = code)
            c.students.add(request.user)
            c.save()

            return redirect('CourseHome')

    else:
        form = CourseJoinForm()

    return render(request, 'courses/join.html', {'form': form ,'wrong': False })

'--------------------------------------------------------------'

def course(request,course_id):
    
    if not request.user.is_authenticated:
        return redirect('login')
    
    c = Course.objects.get(pk = course_id)
    names = [ s.username for s in c.students.all() ]
    uname = request.user.username
    if uname not in names and uname != c.instructor.username:
        return redirect('CourseHome')

    args = {
        'Instructor': c.instructor,
        'Students': c.students.all(),
        'course': c,
        'assignments': c.assignment_set.all(),
    }
    return render(request,'courses/coursepage.html',args)

def assign_create(request,course_id):
    
    if not request.user.is_authenticated:
        return redirect('login')
        
    c = Course.objects.get(pk = course_id)
    if c.instructor.username != request.user.username:
        return redirect('CourseHome')  

    if request.method == 'POST':
        form  = AssignCreationForm(request.POST,request.FILES)
        if form.is_valid():
            assign_name = form.cleaned_data['name']
            ref = form.cleaned_data['weblink']
            msg = form.cleaned_data['statement']
            #f_name = form.cleaned_data['file_name']
            a_file = request.FILES.get('file',False)

            a = Assignment.objects.create(name = assign_name,course = c)
            a.statement = msg
            a.link = ref

            if a_file:   #checking if file exists or not.
                a.file  = a_file
                a.file_name = a.file.name.split("/")[-1]
            a.save()

            return redirect('coursepage',course_id = c.pk)
    else:
        form = AssignCreationForm()

    args = {
        'Instructor': c.instructor,
        'Students': c.students.all(),
        'course': c,
        'form': form,
        'assignments': c.assignment_set.all()
    }
    return render(request,'courses/assign_create.html',args)


def assign(request,course_id,assign_id):
    a = Assignment.objects.get(pk = assign_id)
    c = Course.objects.get(pk = course_id )

    if not request.user.is_authenticated:
        return redirect('login')

    c = Course.objects.get(pk = course_id)
    names = [ s.username for s in c.students.all() ]
    uname = request.user.username
    if uname not in names and uname != c.instructor.username:
        return redirect('CourseHome')


    if request.method == "POST":
        form = AssignmentSubmitForm(request.POST,request.FILES)
        if form.is_valid():
            s_file = request.FILES.get('file',False)

            if FileSubmission.objects.filter(user = request.user,assignment = a).exists():#resubmission.
                s = FileSubmission.objects.get(user = request.user,assignment = a)
            else:
                s = FileSubmission.objects.create(user = request.user, assignment = a)
            if s_file:
                s.file = s_file
                s.file_name = s.file.name.split("/")[-1]
            s.save()
                
        return redirect('assign_page',course_id = c.pk,assign_id = a.pk)
    else:
        form = AssignmentSubmitForm()

    
    subms = list(a.filesubmission_set.all())
    submitted = False
    for sub in subms:
        if request.user.username == sub.user.username:
            submitted = True
            break
    if submitted:
        mysubmission = FileSubmission.objects.get(user = request.user,assignment = a)
    else:
        mysubmission = {'feedback': 'You Did Not Submit'}

    instruct = True
    if c.instructor.username != request.user.username:
        instruct = False
        
    args = {
        'form': form,
        'assign': a,
        'course': c,
        'submissions': list(a.filesubmission_set.all()),
        'submitted': submitted,
        'mysub': mysubmission,
        'instruct': instruct
    }
    return render(request,'courses/assign_page.html',args)


def submissions(request,course_id,assign_id):
    a = Assignment.objects.get(pk = assign_id)
    c = Course.objects.get(pk = course_id )

    if not request.user.is_authenticated:
        return redirect('login')

    uname = request.user.username
    if uname != c.instructor.username:
        return redirect('CourseHome')

    args = {
        'assign': a,
        'course': c,
        'submissions': list(a.filesubmission_set.all()),
    }
    return render(request,'courses/submissions.html',args)

def feedback(request,course_id,assign_id):
    a = Assignment.objects.get(pk = assign_id)
    c = Course.objects.get(pk = course_id )

    if not request.user.is_authenticated:
        return redirect('login')

    uname = request.user.username
    if uname != c.instructor.username:
        return redirect('CourseHome')

    args = {
        'assign': a,
        'course': c,
        'submissions': list(a.filesubmission_set.all()),
    }
    return render(request,'courses/feedback.html',args)




    #FEED BACK FORM-----MODEL SAVE FEED BACK, CORRECTED  =TRUE;
    #CHANGE PASSWORD ETC..