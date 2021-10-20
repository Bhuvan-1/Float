from django import forms

class CourseCreationForm(forms.Form):
    name = forms.CharField(label='Course name', max_length=100)

class CourseJoinForm(forms.Form):
    code = forms.CharField(label='Enter Course Code', max_length=10)

class AssignCreationForm(forms.Form):
    name = forms.CharField(label='Assignment name', max_length=50,required=True)
    file = forms.FileField(label='Problem File',required=False)
    #file_name = forms.CharField(label='FileName', max_length=50)
    weblink = forms.URLField(label='URL link',required=False)
    statement = forms.CharField(
            widget= forms.Textarea(
                attrs={'style': 'border-color: orange;' 'width: 80%' 'height: 200px' 'padding: 12px 20px;' 'border: 2px solid #ccc;' 'border-radius: 15px;''background-color: #f8f8f8;' }
            ),
            label='Description',
            required=True,
            max_length=300
    )
    marks = forms.IntegerField(label='Max Marks',required=True)


class AssignmentSubmitForm(forms.Form):
    file = forms.FileField(label='Submission File',required=True)

class FeedbackForm(forms.Form):
    feedback = forms.CharField(
        widget= forms.Textarea(
            attrs={'style': 'border-color: orange;' 'width: 80%;' 'height: 400px' 'padding: 12px 20px;' 'border: 2px solid #ccc;' 'border-radius: 15px;''background-color: #f8f8f8;' }
        ),
        label='Feedback',
        required=True,
        max_length=300
    )
    grade = forms.IntegerField(label='Grade',required=True)
