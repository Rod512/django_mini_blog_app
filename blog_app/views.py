from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm, LoginForm


def home(request):
    return render(request, 'blog_app/home.html')

def about(request):
    return render(request, 'blog_app/about.html')

def contact(request):
    return render(request, 'blog_app/contact.html')

def dasboard(request):
    return render(request, 'blog_app/dashboard.html')

def user_signup(request):
    form = SignupForm()
    return render(request, 'blog_app/signup.html', {'form': form})

def user_login(request):
    form = LoginForm()
    return render(request, 'blog_app/login.html', {'form':form})

def user_logout(request):
    return HttpResponseRedirect('/')