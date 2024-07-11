from django.shortcuts import render
def getfees1(request):
    d = {'a':100} 
    return render(request,'fees/fees1.html',d)

def getfees2(request):
    d = {'a':200} 
    return render(request,'fees/fees2.html',d)
# Create your views here.
