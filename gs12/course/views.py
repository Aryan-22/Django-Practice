from django.shortcuts import render

def getcourse(request):
    return render(request,'course/info.html',{'name':'Django'})

# Create your views here.


