from django.shortcuts import render
from django.http import HttpResponse
def get_course1(request):
   d = {'a':200,'b':300}
   return render(request,'course/course1.html',context=d)

# Create your views here.
