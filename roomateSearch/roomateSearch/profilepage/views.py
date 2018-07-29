from django.shortcuts import render
from .forms import profileForm, changeAnswersForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from homepage.models import RoomateUser
from django.contrib.auth.models import User
# Create your views here.
def profileP(request, pk):
    if(pk == request.user.username):
        if(request.method == 'POST'):
            pform = profileForm(request.POST)       
            if(pform.is_valid()):
                if(pform.cleaned_data['action'] == "logout"):
                    logout(request)
                    return HttpResponseRedirect('/') 
                if(pform.cleaned_data['action'] == "open chat"):
                    return HttpResponseRedirect('/profileP/mainChatPage')
                if(pform.cleaned_data['action'] == "change survey"):
                    return HttpResponseRedirect('/changeS')
        else:
            pform = profileForm()
            matches = RoomateUser.objects.filter(answer_one = request.user.roomateuser.answer_one, answer_two = request.user.roomateuser.answer_two,
                                                 answer_three = request.user.roomateuser.answer_three, answer_four = request.user.roomateuser.answer_four,
                                                 answer_five = request.user.roomateuser.answer_five)     
            matchusernames = []
            for match in matches:
                if(match.user.username != request.user.username):
                    matchusernames.append(match.user.username)
        return render(request, 'homepage/hpageWithVars.html', {'pform' : pform , 'matchusernames' : matchusernames})
    else:
        oUser = User.objects.get(username = pk)
        matches = RoomateUser.objects.filter(answer_one = oUser.roomateuser.answer_one, answer_two = oUser.roomateuser.answer_two,
                                                 answer_three = oUser.roomateuser.answer_three, answer_four = oUser.roomateuser.answer_four,
                                                 answer_five = oUser.roomateuser.answer_five)     
        matchusernames = []
        for match in matches:
            if(match.user.username != oUser.username):
                matchusernames.append(match.user.username)
        return render(request, 'homepage/otherUserPageWithVars.html', {'oUser' : oUser , 'matchusernames' : matchusernames})

def changeSurvey(request):
    if(request.method == 'POST'):
        caform = changeAnswersForm(request.POST)
        if(caform.is_valid()):
            request.user.roomateuser.answer_one = caform.cleaned_data["answer_one"]
            request.user.roomateuser.answer_two = caform.cleaned_data["answer_two"]
            request.user.roomateuser.answer_three = caform.cleaned_data["answer_three"]
            request.user.roomateuser.answer_four = caform.cleaned_data["answer_four"]
            request.user.roomateuser.answer_five = caform.cleaned_data["answer_five"]
            request.user.save()
            return HttpResponseRedirect('/profileP/'+request.user.username)
    else:
        caform = changeAnswersForm()
    return render(request, 'homepage/hpageWithVars.html', {'caform' : caform})
