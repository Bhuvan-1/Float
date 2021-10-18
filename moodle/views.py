from django.shortcuts import render , redirect , get_object_or_404

from django.http import HttpResponse, response
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from moodle.forms import SignupForm
import requests


def dashboard(request):

	if not request.user.is_authenticated:
		return redirect('login')

	return render(request,'accounts/dashboard.html')



#view corresponding to the signup page
def sign_up(request):
	if request.method == 'POST':
		#form = UserCreationForm(request.POST)
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts/login/')
		else:
			#form = UserCreationForm()
			form = SignupForm()
			args = { 'form': form , 'success' : False }
			return render(request,'accounts/sign_up.html',args)
	else:
		#form = UserCreationForm()
		form = SignupForm()
		args = {'form': form , 'success' : True }
		return render(request,'accounts/sign_up.html',args)
