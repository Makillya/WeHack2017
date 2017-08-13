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
    return redirect(request, "messaging:index")
