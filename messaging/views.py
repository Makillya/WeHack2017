# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'messaging/index.html')

# Add message to DB
def addMessage(request,addresseeId):
    if request.method == "POST":
        creatorId=request.session["currentUser"]
        message=Message.objects.add(request.POST, creatorId, addresseeId)
        if not message[0]:
            for i in range(0, len(message[1])):
                messages.error(request, message[1][i])
            return redirect('loginreg:index')
        else:
            request.session['currentUser'] = message[1].id
            return redirect ('loginreg:success')

            
