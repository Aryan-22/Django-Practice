from django.shortcuts import render
from datetime import datetime
def getcourse1(request):
    d = datetime.now()
    return render(request,'course/course1.html',{'dt':d})

def getcourse2(request):
    d = {'a':'javascript'}
    return render(request,'course/course2.html',d)
# Create your views here.
