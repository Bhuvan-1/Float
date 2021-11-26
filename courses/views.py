from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.db.models.signals import post_save
from django.contrib.auth.models import User

import courses
from .forms import AssignCreationForm, AssignmentSubmitForm, CourseCreationForm , CourseJoinForm, FeedbackForm
from .models import Assignment, Course, FileSubmission #, Student , Instructor
import random
import datetime
# Create your views here.



def generate_code(): #function to generate random course code.
    s = ""
    for i in range(0,6):
        c = random.randint(65,90)
        s += chr(c)
    return s

'''--------------------------------------------------------------'''

#courses_home
#added-Student an instructor ToDO list
#added TA courses as well ... 24/11.
#added percentages--to render corrctly....26/11.
def course_info(request):

    if not request.user.is_authenticated:
        return redirect('login')

    u = User.objects.get(pk = request.user.pk )

    Itodo_List = [] #list of TO-DO assignments for 'I'nstructors ['S' ==> students, 'I' ==> Instructors ]
    Stodo_List = [] #list of TO-DO of students
    TAtodo_List = [] #for TA's


    PercI_List = [] #list of percentage of course completed.
    PercS_List = []
    PercT_List = []

    now = datetime.datetime.now()
    for course in u.ins_courses.all():
        graded_count = 0
        assign_count = 0
        for assign in course.assignment_set.all():
            if now > assign.deadline:
                graded=True
                for sub in assign.filesubmission_set.all():
                    if sub.corrected == 'NO':
                        graded = False
                        break
                if not graded:
                    Itodo_List.append(assign)
                else:
                    graded_count += 1
            assign_count += 1
        if assign_count == 0:
            PercI_List.append(100)
        else:
            PercI_List.append(int((graded_count*100)/assign_count))

    for course in u.stud_courses.all():
        print(1)
        assign_count = 0
        sub_count = 0
        for assign in course.assignment_set.all():
            if now < assign.deadline:
                submitted=False
                for sub in assign.filesubmission_set.all():
                    if sub.user.username == request.user.username:
                        submitted = True
                        break
                if not submitted:
                    Stodo_List.append(assign)
                else:
                    sub_count += 1
            else:
                submitted=False
                for sub in assign.filesubmission_set.all():
                    if sub.user.username == request.user.username:
                        submitted = True
                        break
                if submitted:
                    sub_count += 1
            assign_count += 1
        if assign_count == 0:
            PercS_List.append(100)
        else:
            PercS_List.append(int((graded_count*100)/assign_count))

    for course in u.ta_courses.all():
        graded_count = 0
        assign_count = 0
        for assign in course.assignment_set.all():
            if now > assign.deadline:
                graded=True
                for sub in assign.filesubmission_set.all():
                    if sub.corrected == 'NO':
                        graded = False
                        break
                if not graded:
                    TAtodo_List.append(assign)
                else:
                    graded_count += 1
            assign_count += 1
        if assign_count == 0:
            PercT_List.append(100)
        else:
            PercT_List.append(int((graded_count*100)/assign_count))

    for i in range(len(PercS_List)):
        PercS_List[i] = str(PercS_List[i]) + '%'

    for i in range(len(PercI_List)):
        PercI_List[i] = str(PercI_List[i]) + '%'

    for i in range(len(PercT_List)):
        PercT_List[i] = str(PercT_List[i]) + '%'


    args = {
        'scourses': u.stud_courses.all(),
        'icourses': u.ins_courses.all(),
        'Tcourses': u.ta_courses.all(),
        'Itodo': Itodo_List,
        'Stodo': Stodo_List,
        'Ttodo': TAtodo_List,
        'Perc_S': PercS_List,
        'Perc_I': PercI_List,
        'Perc_T': PercT_List,
    }
        
    return render(request,'courses/home.html',args)

#created TA join code as well
def create(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            course_name = form.cleaned_data['name']
            code = generate_code()
            TAcode = generate_code()

            e = Course.objects.all().filter(joincode__in = [code, TAcode] ).count()
            n = Course.objects.all().filter(TAjoincode__in = [code, TAcode] ).count()
            while e != 0 or n != 0:
                code = generate_code()
                TAcode = generate_code()
                e = Course.objects.all().filter(joincode__in = [code, TAcode] ).count()
                n = Course.objects.all().filter(TAjoincode__in = [code, TAcode] ).count()

            e = Course.objects.all().filter(name = course_name).count()
            if( e != 0): #Name already exists.
                args = {'form': form, 'wrong': True}
                return render(request, 'courses/create.html', args)

            c = Course.objects.create(instructor = request.user)
            c.name = course_name
            c.joincode = code
            c.TAjoincode = TAcode
            c.save()

            return redirect('CourseHome')

    else:
        form = CourseCreationForm()

    return render(request, 'courses/create.html', {'form': form, 'wrong': False})
'---------------------------------------------------------------------------'

#added TA join also.
def join(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CourseJoinForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            code = form.cleaned_data['code']
            e = Course.objects.all().filter(joincode = code).count()
            n = Course.objects.all().filter(TAjoincode = code).count()

            if( e == 0 and n == 0):  #incorrect course code.
                args = {'form': form, 'wrong': True}
                return render(request, 'courses/join.html', args)
            
            if e != 0:
                c = Course.objects.get(joincode = code)
                c.students.add(request.user)
                c.save()
            elif n != 0:
                c = Course.objects.get(TAjoincode = code)
                c.TAs.add(request.user)
                c.save()             

            return redirect('CourseHome')

    else:
        form = CourseJoinForm()

    return render(request, 'courses/join.html', {'form': form ,'wrong': False })

'--------------------------------------------------------------'

#course_page
#Addded TA check! .. 24/11
#added now time, to color the assignments.
def course(request,course_id):
    
    if not request.user.is_authenticated:
        return redirect('login')
    
    c = Course.objects.get(pk = course_id)
    Snames = [ s.username for s in c.students.all() ]
    Tnames = [ s.username for s in c.TAs.all() ]
    uname = request.user.username
    if uname not in (Snames + Tnames) and uname != c.instructor.username:
        return redirect('CourseHome')

    args = {
        'Instructor': c.instructor,
        'Students': c.students.all(),
        'TAs': c.TAs.all(),
        'course': c,
        'assignments': c.assignment_set.all(),
        'nowtime': datetime.datetime.now(),
    }
    return render(request,'courses/coursepage.html',args)


#added the assign_deadline[ in form too] while saving form into an object. 22/11____23/11[bug]
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
            dedline = form.cleaned_data['deadline']
            #f_name = form.cleaned_data['file_name']
            a_file = request.FILES.get('file',False)

            a = Assignment.objects.create(name = assign_name,course = c,deadline = dedline)
            a.statement = msg
            a.link = ref
            a.maxmarks = form.cleaned_data['marks']

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


#added the deadline to render 22/11.
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

    deadline = a.deadline
        
    args = {
        'form': form,
        'assign': a,
        'course': c,
        'submissions': list(a.filesubmission_set.all()),
        'submitted': submitted,
        'mysub': mysubmission,
        'instruct': instruct,
        'deadline': deadline,
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

def feedback(request,course_id,assign_id,sub_id):
    a = Assignment.objects.get(pk = assign_id)
    c = Course.objects.get(pk = course_id )
    s = FileSubmission.objects.get(pk = sub_id)

    if not request.user.is_authenticated:
        return redirect('login')

    uname = request.user.username
    if uname != c.instructor.username:
        return redirect('CourseHome')


    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['feedback'])
            s.feedback = form.cleaned_data['feedback']
            s.corrected = 'YES'
            s.grade = form.cleaned_data['grade']
            s.save()

            return redirect('submissions',course_id,assign_id)
    else:
        if s.corrected == "YES":
            form = FeedbackForm({'feedback': s.feedback})
        else:
            form = FeedbackForm()

    args = {
        'assign': a,
        'course': c,
        'submissions': list(a.filesubmission_set.all()),
        'sub': s,
        'form': form
    }
    return render(request,'courses/feedback.html',args)


    #CHANGE PASSWORD ETC..

def grades(request,course_id):
    return HttpResponse("hello")


def participants(request,course_id):
    return HttpResponse("hello")

def forum(request,course_id):
    return HttpResponse("hello")