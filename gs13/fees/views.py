from django.shortcuts import render
def getfees1(request):
    return render(request,'fees/fees1.html',
                  {'Title':'Django fees','course':'django','charge':300})
# Create your views here.
