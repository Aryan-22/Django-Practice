from django.shortcuts import render

def home(request):
    return render(request,'core/home.html',{"d":"django"})
def about(request):
    return render(request,'core/about.html',{'abc':'/about'})
# Create your views here.
