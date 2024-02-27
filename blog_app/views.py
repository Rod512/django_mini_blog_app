from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm, LoginForm, Postform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/home.html',{'posts':posts})

def about(request):
    return render(request, 'blog_app/about.html')

def contact(request):
    return render(request, 'blog_app/contact.html')

def dasboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all() 
        return render(request, 'blog_app/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

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
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog_app/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Postform(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title= title, desc = desc)
                pst.save()
                form = Postform()
        else:
            form = Postform()
        return render(request, 'blog_app/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    

def update_post(request, id):
    if request.user.is_authenticated:
        return render(request, 'blog_app/updatepost.html')
    else:
        return HttpResponseRedirect('/login/')
    
def delete_post(request, id):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')