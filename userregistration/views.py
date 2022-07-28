from click import password_option
from django.shortcuts import render
from flask import render_template, request
from django.http import HttpResponse
from userregistration import models
from django.contrib import messages
from django.shortcuts import redirect







# Create your views here.


def index(request):
    return render(request, 'login.html')

def register(request):
    return render(request,'registration.html' )

def registeruser(request):
    if request.method == "POST":
       
      first_name=request.POST['firstname']
      last_name=request.POST['lastname']
      dob=request.POST['Dateofbirth']
      emailid=request.POST['email']
      user_name=request.POST['username']
      pwdd=request.POST['password']
      credintials=models.registeredUsers(  firstname=first_name, lastname=last_name, Dateofbirth=dob,username=user_name, email=emailid,
                                        password=pwdd,Reenterpassword="",post="")
      credintials.save()
      return render(request,'login.html')

def sucessfullUser(request):
    Username=request.POST['username']
    Password=request.POST['password']
    if(models.registeredUsers.objects.filter(username=Username, password=Password).exists()):
            return render(request, "profile.html")
    else:
          messages.error(request, 'username or password not correct')
          return redirect('/login')



