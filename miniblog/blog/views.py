from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate,login,logout 
from .forms import SignUpForm,LoginForm,AddPostForm
from .models import Post
from django.contrib import messages
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{"posts":posts})


def about(request):
    return render(request,'blog/about.html')


def contact(request):
    return render(request,'blog/contact.html')
def dashboard(request):
    if request.user.is_authenticated:
        
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()

        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,"groups":gps})
    return HttpResponseRedirect('/login/')
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')  # Redirect already authenticated users to the dashboard
    
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data["username"]
            upass = form.cleaned_data["password"]
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successful!!!")
                return HttpResponseRedirect('/dashboard/')
    else:
        form = LoginForm()
    
    return render(request, 'blog/login.html', {'form': form})  # Render login form for unauthenticated users



def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"Congratulations You have become an author!!")
            group = Group.objects.get(name = 'Author')
            user.groups.add(group)
    else:
        form = SignUpForm()


    
    return render(request,"blog/signup.html",{"fm":form})


def add_post(request):
    if request.user.is_authenticated:
        
        if request.method == "POST":
            form = AddPostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']

                pst = Post(title = title,desc = desc,user = request.user)
                pst.save()
                messages.success(request,"Post add Successfully!!")
                
                return HttpResponseRedirect('/dashboard/')
        else:
            form = AddPostForm()

        return render(request,'blog/addpost.html',{"form":form})
    else:
        return HttpResponseRedirect('/login/')
    

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk = id)
            form = AddPostForm(request.POST,instance = pi)
            if form.is_valid():
                messages.success(request,"Post Updated Successfully!!!")
                form.save()
        else:
            pi = Post.objects.get(pk = id)
            
            form = AddPostForm(instance = pi)
        return render(request,'blog/updatepost.html',{"form":form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk = id)
            if request.user == pi.user or request.user.is_superuser:
                pi.delete()
                messages.success(request,"Post Deleted Successfully!!!")
                return HttpResponseRedirect('/dashboard/')
            return HttpResponseRedirect('/dashboard/')
        return HttpResponseRedirect('/dashboard/')
            


    else:
        return HttpResponseRedirect('/login/')

