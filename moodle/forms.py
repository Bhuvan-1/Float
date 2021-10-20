from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from courses.models import Course

class SignupForm(UserCreationForm):	#creating our custom registration form
	first_name = forms.CharField(required = True )
	email = forms.CharField(required=True)
	
	class Meta:
		model = User
		fields = (
		   'username',
		   'password1',
		   'password2',
		   'email',
		   'first_name',
		   'last_name',
		)
		
	def save(self, commit = True):
		user = super(SignupForm, self ).save(commit = False )
		user.first_name  = self.cleaned_data['first_name']
		user.last_name  = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		
		if commit:
			user.save()
		return user
