from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('movieapp:allmovies')
            except IntegrityError:
                return render(request, 'accounts/signupuser.html', {'form': UserCreationForm(), 'error': 'User Already Exist '})
        else:
            return render(request, 'accounts/signupuser.html', {'form': UserCreationForm(), 'error': 'Password did no match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and Password did not  match '})
        else:
            login(request, user)
            return redirect('movieapp:allmovies')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('movieapp:allmovies')
