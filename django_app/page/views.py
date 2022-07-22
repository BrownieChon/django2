from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import member, members
from django.core.mail import send_mail
# Create your views here.

def chonpat(request):
    template = loader.get_template('chonpat.html')
    return HttpResponse(template.render())
def index(request):
    template = loader.get_template('index.html')
    session = 0
    context ={
        'session' : session,
    }
    return HttpResponse(template.render(context,request))

def login(request):
    user = request.POST['username']
    password = request.POST['password']
    user_check = members.objects.filter(username = user).values('password')
    for x in user_check:
        password_check = members.objects.filter(password = password).values('password')
        for y in password_check:
            if x == y:
                    template = loader.get_template('success.html')
                    welcome = members.objects.filter(username = user).values()
                    context ={
                            'welcome' : welcome,
                    }
                    return HttpResponse(template.render(context,request))
        else:
           return render(request, 'error.html') 
    else:
        return render(request, 'error.html')

def index_member(request, members_id):
    template = loader.get_template('index.html')
    display = members.objects.filter(id = members_id).values()
    data = members.objects.all()
    session = 1
    context ={
        'display' : display,
        'session' : session,
        'data' : data,
    }
    return HttpResponse(template.render(context,request))
    
    
def logout(request):
    return HttpResponseRedirect(reverse('index'))



def forget(request):
    return render(request, 'forgetpassword.html')
    

def forgetpassword(request):
    user = request.POST['username']
    password = members.objects.filter(username = user).values()
    for x in password:
        password_check = members.objects.filter(password = password).values()
    email = members.objects.filter(username = user).values()
    for y in email:
        email_check = members.objects.filter(password = password).values()
    check_pass = password_check
    check_mail = email_check
    send_mail(
    'Your Password Here',
    'check_pass',
    'chonpatadmin@gmail.com',
    [' check_mail'],
    fail_silently=False,
    )
    session = 3
    context = {
        'session' : session
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context,request))

def register(request):
    return render(request, 'register.html')

def regist(request):
    user = request.POST['username']
    password = request.POST['password']
    re_password = request.POST['re_password']
    email = request.POST['email']
    name = request.POST['name']
    lastname = request.POST['lastname']
    usercheck = members.objects.filter(username = user).values()
    for user in usercheck:
        return render(request, 'error_register.html')
    else:
        if password == re_password:
            excute = members(username = user, password = password, email = email, Name = name, Lastname = lastname)
            excute.save()
            template = loader.get_template('success.html')
            welcome = members.objects.filter(username = user).values()
            context ={
                'welcome' : welcome,
            }
            return HttpResponse(template.render(context,request))
        else:
            return render(request, 'error.html')