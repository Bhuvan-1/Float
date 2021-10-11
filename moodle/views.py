from django.shortcuts import render , redirect , get_object_or_404

from django.http import HttpResponse, response
from django.contrib.auth.models import User


def home(request):
    return render(request,'base.html')