from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth import *
from misterprofessor.models import *


def index(request, code=""):
    context={}
    #===========================================================================
    # profiles = list()
    # profiles.append(Profile(user = request.user))
    #===========================================================================
    p = Profile.objects.get(user = request.user)
    ss = Subscription.objects.filter(student = request.user)
    ls = list()
    for s in ss:
        ls.append(Lesson.objects.filter(course = s.course))
    
    context['profile'] = p
    context['lessons'] = ls
    if code!= "":
        c = Course.objects.get(id = code)
        context['subscription'] = "You succesflully subcribe to "+ c.name
    return addMenu(request, 'index.html', context)
    
def course(request, code):  
    context={}
    c = Course.objects.get(id = code)
    t = Profile.objects.get(id = c.teacher.id)
    ls = Lesson.objects.filter(course = c)
    
    context['course'] = c
    context['teacher'] = t
    context['lessons'] = ls
    
    return addMenu(request, 'first.html', context)


def profile(request, code=""):
    if code=="":
        usertoprofile = request.user
    else:
        usertoprofile = User.objects.filter(id = code)
    context={}  
    els = Profile.objects.get(user = usertoprofile)
    context['els'] = els
    return addMenu(request, 'index.html', context)

def course_subscription(request, code):
    #code = request.POST['coursecode']
    code = 2
    c = Course.objects.get(id = code)
    s = Subscription(student = request.user, course = c)
    s.save()
    return redirect('postSubscription', code)
    
    
#===============================================================================
# def search(request):
#     return#TODO
#===============================================================================

def settings(request):   
    context={}
    myprofile = Profile.objects.get(user = request.user)
    context['form'] = ProfileForm(instance=myprofile)
    return addMenu(request, 'settings.html', context)

def settingspost(request):
    myprofile = Profile.objects.get(user = request.user)
    p = ProfileForm(request.POST, instance=myprofile)
    p.save()
    return redirect('index')
#===============================================================================
# def user(request, uname=""):
#     if uname=="":
#         uname = request.user.username    
#     context={}
#     uname = uname+""
#     uuser = User.objects.filter(username = uname)
#     profile = Profile.objects.get(user = uuser)
#     context['p'] = profile
#     context['r'] = request.user
#     return addMenu(request, 'user.html', context)
#===============================================================================

def search(request):
    context={}
    context['form']= SearchForm()
    return addMenu(request, 'search.html', context)
    
def searchresult(request):
    context={}
    lang = request.POST.getlist('languages')
    cs = list()
    for l in lang:
        for c in Course.objects.filter(language=l):
            cs.append(c)
    context['courses'] = cs
    return addMenu(request, 'searchresult.html', context)   
    
def first(request):
    context={}
    form = AuthenticationForm()
    context['form'] = form
    return render(request, 'first.html', context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/index')
        else:
            return redirect('/error')
    else:
        return redirect('/error')

def error(request):
    context={}
    return render(request, 'error.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')



#===============================================================================
# 
# Function used to fill the context with extra
# content. Eg. Menu
#===============================================================================

def addMenu(request, template='base.html', context={}):
    context ['menuelements'] = MenuElement.objects.all
    return render(request, template, context)
    
