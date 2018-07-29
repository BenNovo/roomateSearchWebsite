# Create your views here.


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm, RoomateUserForm, chooseForm, loginForm
from django.contrib.auth import login, authenticate
def index(request):
    if(request.method == "GET"):
        cform = chooseForm()
        return render(request, 'homepage/OtherTemplate.html', {'cform' : cform})
    if(request.method == "POST"):
        cform = chooseForm(request.POST)
        if(cform.is_valid()):
            if(cform.cleaned_data["action"] == "login"):
                return HttpResponseRedirect(reverse('loginP'))
            else:
                return HttpResponseRedirect(reverse('createUserP'))
        else:
            return render(request, 'homepage/OtherTemplate.html', {'cform' : cform})
            
def logIn(request):
    if(request.method == 'POST'):
        lform = loginForm(request.POST);
        if(lform.is_valid()):
            usernamehere = lform.cleaned_data['username']
            raw_password = lform.cleaned_data.get('password')
            user = authenticate(username=usernamehere, password=raw_password)
            if(user is not None):
                login(request, user)
                return HttpResponseRedirect('/profileP/'+user.username)
    else:
        lform = loginForm();
    return render(request, 'homepage/OtherTemplate.html', {'lform' : lform})
        
def createUser(request):
    if(request.method == 'POST'):
        uform = UserForm(request.POST)
        ruform = RoomateUserForm(request.POST, request.FILES)
        if(uform.is_valid() & ruform.is_valid()):       
            user = uform.save()
            raw_password = uform.cleaned_data.get('password')
            user.set_password(raw_password)
            user.refresh_from_db()
            user.roomateuser.answer_one = ruform.cleaned_data["answer_one"]
            user.roomateuser.answer_two = ruform.cleaned_data["answer_two"]
            user.roomateuser.answer_three = ruform.cleaned_data["answer_three"]
            user.roomateuser.answer_four = ruform.cleaned_data["answer_four"]
            user.roomateuser.answer_five = ruform.cleaned_data["answer_five"]
            user.roomateuser.bio = ruform.cleaned_data["bio"]
            user.roomateuser.picture = ruform.cleaned_data["image"]
            user.save()           
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/profileP/'+user.username)                 
    else:
        uform = UserForm()
        ruform = RoomateUserForm()
    return render(request, 'homepage/OtherTemplate.html', {'uform' : uform, 'ruform' : ruform})
    
