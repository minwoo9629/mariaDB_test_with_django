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
            nick_name = request.POST['nickname']
            sid = request.POST['studentid']
            user_phone = request.POST['userphone']
            user_profile = ProfileUser(user=user, NickName=nick_name, StudentID=sid)
            user_phone = UserPhone(user=user, userphone=user_phone)
            user_profile.save()
            user_phone.save()
            return redirect('login')
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return render(request, 'login.html')
