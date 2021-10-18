from django import forms

class CourseCreationForm(forms.Form):
    name = forms.CharField(label='Course name', max_length=100)

class CourseJoinForm(forms.Form):
    code = forms.CharField(label='Enter Course Code', max_length=10)