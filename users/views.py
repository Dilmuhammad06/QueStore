from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                msg = 'Malumotlar xato kiritilgan'
                return render(request, 'login.html',{'form':form,'msg':msg})
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')