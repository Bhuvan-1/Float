from django import forms

class CourseCreationForm(forms.Form):
    name = forms.CharField(label='Course name', max_length=100)

class CourseJoinForm(forms.Form):
    code = forms.CharField(label='Enter Course Code', max_length=10)

class AssignCreationForm(forms.Form):
    name = forms.CharField(label='Assignment name', max_length=50,required=True)
    file = forms.FileField(required=False)
    #file_name = forms.CharField(label='FileName', max_length=50)
    weblink = forms.URLField(required=False)
    statement = forms.CharField(label = 'Description',max_length=300,required=True)

class AssignmentSubmitForm(forms.Form):
    file = forms.FileField(required=True)

    