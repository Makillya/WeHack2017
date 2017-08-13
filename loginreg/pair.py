from models import User
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'search.html')  #set input source

def search(request):
    byTitle = True
    inputs = ''
    currentID = request.session['currentUser'] #get current user id
    if currentID <> None:
        isMentor = (User.objects.get(id=currentID).user_type == 'mentor')
    if request.method == 'POST':
        userInput=request.POST
        inputs = userInput["input"]
        if userInput["by"] == 'zipcode': #get searchBy
            byTitle = False
        elif userInput["by"] <> 'title':
            return None
    data = search2(isMentor, byTitle, inputs)
    response = HttpResponse(data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"' 
    return response #return table by csv
    
def search2(isMentor, byTitle, inputs):
    if inputs == '':
        return showAll(isMentor)
    if byTitle:
        if isMentor:
            return User.objects.filter(user_type='mentee').filter(title=inputs).order_by('last_name')
        else:
            return User.objects.filter(user_type='mentor').filter(title=inputs).order_by('last_name')
    else:
        if isMentor:
            return User.objects.filter(user_type='mentee').filter(zipcode=inputs).order_by('last_name')
        else:
            return User.objects.filter(user_type='mentor').filter(zipcode=inputs).order_by('last_name')
        
def showAll(isMentor):
    if isMentor:
        return User.objects.filter(user_type='mentee')
    else:
        return User.objects.filter(user_type='mentor')
