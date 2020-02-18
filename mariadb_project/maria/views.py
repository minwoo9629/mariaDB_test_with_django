from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import ProfileUser, UserPhone
# Create your views here.
def search(request):
    alluserdata = User.objects.all()
    return render(request, 'search.html',{'alluserdata':alluserdata})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            nname = request.POST['nickname']
            sid = request.POST['studentid']
            uphone = request.POST['userphone']
            userprofile = ProfileUser(user=user, NickName=nname, StudentID=sid)
            userphone = UserPhone(user=user, userphone=uphone)
            userprofile.save()
            userphone.save()
            return redirect('login')

    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return render(request, 'login.html')