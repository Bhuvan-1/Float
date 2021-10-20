from django.shortcuts import render , redirect , get_object_or_404

from django.http import HttpResponse, response
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from moodle.forms import SignupForm,ProfileChangeForm
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


def profile_change(request):

	if not request.user.is_authenticated:
		return redirect('login')

	if request.method == 'POST':
		form = ProfileChangeForm(request.POST,instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	else:
		form = ProfileChangeForm(instance = request.user)
	args = {'form': form }
	return render(request,'accounts/profile_change.html',args)


def change_pass(request):
	
	if not request.user.is_authenticated:
		return redirect('login')

	if request.method == 'POST':
		form = PasswordChangeForm(data = request.POST,user = request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user) 
			return redirect('dashboard')
		else:
			form = PasswordChangeForm(user = request.user)
			args = {'form': form , 'success': False}
			return render(request,'accounts/password_change.html',args)

	else:
		form = PasswordChangeForm(user = request.user)
		args = {'form': form , 'success': True}
		return render(request,'accounts/password_change.html',args)

