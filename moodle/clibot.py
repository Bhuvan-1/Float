from django.contrib.auth.models import User
from courses.models import Course


def reply(question,user_id):
    if question == 'ls':
        ans = ''
        u = User.objects.get(pk = user_id)
        I = u.ins_courses.all()

        ans += '[ \''
        for i in I:
            ans += i.name
            ans += ' , '
        return 'Courses:  ' + ans + '\' ]'
    else:
        return 'NULL'

