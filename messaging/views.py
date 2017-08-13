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

def chatHist(request, rec):
    currentID = request.session['currentUser'] #get current user id
    if currentID == None or rec == None:
        return None
    data = Message.objects.filter(creator.id=currentID).filter(addressee.id=rec)
    data = data.join(Message.objects.filter(creator.id=rec).filter(addressee.id=currentID)).sort_by('created_at')
    response = HttpResponse(data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"' 
    return response
