from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todoApplication import models
from todoApplication.models import Todo
from django.contrib.auth import authenticate,login,logout

def signup(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        emailId=request.POST.get('email')
        pwd=request.POST.get('pwd')
        print(fnm,emailId,pwd)
        my_user=User.objects.create_user(fnm,emailId,pwd)
        my_user.save()
        return redirect('/login')
    
    return render(request,'signup.html')

def loginn(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todopage')
        else:
            return redirect('/login')

    return render(request,'login.html')