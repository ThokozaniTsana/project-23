from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )
    else:
        login(request, user)
        return render(request,'authentication/user.html')
        

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
    "username": request.user.username,
    "password": request.user.password
    })

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:show_user')
    else:
        form = SignupForm()
    return render(request, 'authentication/register.html', {'form': form})