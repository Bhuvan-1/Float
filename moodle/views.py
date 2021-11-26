from django.shortcuts import render , redirect , get_object_or_404

from django.http import HttpResponse, response
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from moodle.forms import SignupForm,ProfileChangeForm,Messageform
import requests

from courses.models import Chat, DM

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



def chat(request):

	if not request.user.is_authenticated:
		return redirect('login')

	u = User.objects.all()

	args = {
		'users': u,
		'l':[1,2,3,4,5,6,7,8,9],
	}

	return render(request,'accounts/chat.html',args)

def DM(request,id1,id2):

	usr1 = request.user
	usr2 = User.objects.get(pk = id2)

	S1 = usr1.chats.all()
	S2 = usr2.chats.all()

	S = S1 & S2

	print(len(S))

	# C = Chat.objects.all().filter()
	# exists = False
	# for chat in C:
	# 	if usr1 in chat.users and usr2 in chat.users:
	# 		exists = True
	# 		break

	if len(S) == 0:
		C = Chat.objects.create()
		C.users.add(usr1)
		C.users.add(usr2)
		C.save()

	if request.method == 'POST':
		form = Messageform(request.POST)
		if form.is_valid():
			return redirect(DM,id1,id2)
	else:
		form = Messageform()

	args = {
		'form': form
	}
	return render(request,'accounts/DM.html',args)