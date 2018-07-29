from django.shortcuts import render
from .forms import sendMessageForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from homepage.models import RoomateUser
from django.contrib.auth.models import User
# Create your views here.
def chatroom(request):
    if(request.method == 'POST'):
        smform = sendMessageForm(request.POST)
        if(smform.is_valid()):
            message = smform.cleaned_data['message']
            request.user.roomateuser.messages.append(request.user.username + ": " + message)
            return HttpResponseRedirect('/profileP/'+request.user.username)
        else:
           smform = sendMessageForm(request.POST) 
    else:
        smform = sendMessageForm()
    return render(request, 'homepage/blankTemplateWithVars.html', {'smform' : smform})