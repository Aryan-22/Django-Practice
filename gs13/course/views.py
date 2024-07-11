from django.shortcuts import render
def getcourse1(request):
    return render(request,'course/course1.html',
                  {'Title':'learn django','course':'django'})
# Create your views here.
