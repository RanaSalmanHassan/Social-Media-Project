from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import RegisterForm, Edit_Proifle_Form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from .models import UserProfile
from postapp.models import Follow
# Create your views here.


def Register(request):
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'YOU ARE REGISTERED,NOW LOGIN!')
            return HttpResponseRedirect(reverse('loginapp:login'))
    dict = {'form': form}
    return render(request, 'loginapp/register.html', dict)


def Login(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'LOGGED IN')
                return HttpResponseRedirect(reverse('loginapp:user_profile'))

    dict = {'form': form}
    return render(request, 'loginapp/login.html', dict)


def Logout(request):
    logout(request)
    messages.warning(request,'LOGGED OUT')
    return HttpResponseRedirect(reverse('loginapp:login'))


def user_profile(request):
    
    return render(request, 'loginapp/profile.html')


def edit_profile(request):
    current_user = UserProfile.objects.filter(user=request.user).first()
    form = Edit_Proifle_Form(instance=current_user)
    if request.method == 'POST':
        form = Edit_Proifle_Form(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            form = Edit_Proifle_Form(instance=current_user)
            messages.success(request, 'PROIFLE UPDATED')
            return HttpResponseRedirect(reverse('loginapp:user_profile'))
    dict = {'form': form}
    return render(request, 'loginapp/edit_profile.html', dict)
