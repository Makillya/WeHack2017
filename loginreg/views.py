# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'loginreg/index.html')

# Register user as MENTOR or MENTEE
def register(request):
    print "**********"
    if request.method == 'POST':
        userInput=request.POST
        user = User.objects.register(request.POST)
        if not user[0]:
            for i in range(0, len(user[1])):
                messages.error(request, user[1][i])
            return redirect ('loginreg:index')
        else:
            request.session['currentUser'] = user[1].id
            return redirect('loginreg:profile')


# Login function
def login(request):
    user = User.objects.login(request.POST)
    if not user[0]:
        for i in range(0, len(user[1])):
            messages.error(request, user[1][i])
        return redirect('loginreg:index')
    else:
        request.session['currentUser'] = user[1].id
        return redirect ('loginreg:profile')


# Logout function
def logout(request):
    request.session['currentUser'] = None
    messages.success(request, "You have been successfully logged out!")
    return redirect('spring:main')

def profile(request):
    return render(request, 'loginreg/profile.html')

def search(request):
    return render(request, 'loginreg/search.html')
