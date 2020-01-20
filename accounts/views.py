from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import Userform
from django.contrib import messages
# Create your views here bgg.
def signup(request):
    if request.method=='POST':
        form1=Userform(request.POST)
		
        if form1.is_valid():
            username=form1.cleaned_data['username']
            firstname=form1.cleaned_data['first_name']
            lastname=form1.cleaned_data['last_name']
            emailid=form1.cleaned_data['email']
            password=form1.cleaned_data['password']
            user=User.objects.create_user(username=username, first_name=firstname,last_name=lastname, email=emailid, password=password)
            auth.login(request,user)
            messages.success(request,'User Registration Successfully')
            return redirect('home')
        
            
        # if request.POST['password1']==request.POST['password2']:
        #     try:
        #         user=User.objects.get(username=request.POST['username'])
        #         return render(request,'accounts/signup.html',{'error':'user already exists' })
        #     except User.DoesNotExist:
        #         user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
        #         auth.login(request,user)
        #         return redirect('home')

        # else:
        #     return render(request,'accounts/signup.html',{'error':'password doesn\'t match' })    
    else:
        form1=Userform()
    return render(request,'accounts/signup.html',{'form':form1})
       


def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
           return render(request,'accounts/login.html',{'error':'username or password is wrong' })


    else:   
      return render(request,'accounts/login.html')   



def logout(request):
    if request.method=='POST':
          auth.logout(request)
          return redirect ('home')    