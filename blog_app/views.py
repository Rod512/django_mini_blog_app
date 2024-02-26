from django.shortcuts import render

def home(request):
    return render(request, 'blog_app/home.html')

def about(request):
    return render(request, 'blog_app/about.html')

def contact(request):
    return render(request, 'blog_app/contact.html')

def dasboard(request):
    return render(request, 'blog_app/dashboard.html')

def signup(request):
    return render(request, 'blog_app/signup.html')

def login(request):
    return render(request, 'blog_app/login.html')

def user_logout(request):
    pass