import math
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import ProfileUser, UserPhone
from django.core.paginator import Paginator
# Create your views here.
def search(request):
    alluserdata = User.objects.all().order_by('profileuser__StudentID')
    # order_by에서 다른 모델 객체를 이용할땐 이중 언더바 사용

    paginator = Paginator(alluserdata, 5)    
    # 사용자 정보 5개를 한 페이지로 자름.
    page = request.GET.get('page')
    # request된 페이지 번호를 알아내 변수에 담는다.

    user_page = paginator.get_page(page)
    # 내가 원하는 페이지 가져오기

    show_page_range = 5
    
    max_index = len(paginator.page_range)

    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / show_page_range ) * show_page_range
    end_index = start_index + show_page_range
    if end_index >= max_index:
        end_index = max_index
    
    page_range = paginator.page_range[start_index:end_index]
    context = {'alluserdata':alluserdata, 'user_page':user_page, 'page_range':page_range}
    
    return render(request, 'search.html', context)
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
            user = User.objects.create_user(username=request.POST['user_name'], password=request.POST['password1'])
            nick_name = request.POST['nick_name']
            sid = request.POST['student_id']
            user_phone = request.POST['user_phone']
            user_profile = ProfileUser(user=user, NickName=nick_name, StudentID=sid)
            user_phone = UserPhone(user=user, UserPhone=user_phone)
            user_profile.save()
            user_phone.save()
            return redirect('login')
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return render(request, 'login.html')
