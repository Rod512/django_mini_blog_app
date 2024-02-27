from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render(request, 'blog_app/home.html')

def about(request):
    return render(request, 'blog_app/about.html')

def contact(request):
    return render(request, 'blog_app/contact.html')

def dasboard(request):
    return render(request, 'blog_app/dashboard.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation! you are become an author')
            form.save()
    else:
        form = SignupForm()
    return render(request, 'blog_app/signup.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request = request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog_app/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    return HttpResponseRedirect('/')