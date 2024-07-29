from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def HomePage(request):
    user = request.user
    return render (request,'home.html', {'user': user})

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return render(request, 'signup.html', {})
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            user=authenticate(request,username=uname,password=pass1)
            login(request,user)
            return redirect('home')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html', {})
        
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

#########################################################################
from django.http import JsonResponse
from django.contrib.auth.models import User

def check_username_email(request):
    username = request.GET.get('username', None)
    email = request.GET.get('email', None)

    response = {
        'username_exists': User.objects.filter(username=username).exists(),
        'email_exists': User.objects.filter(email=email).exists(),
    }

    return JsonResponse(response)
