from django.shortcuts import render
def getfees(request):
    return render(request,'fees/info.html',{'cost':100 })

# Create your views here.
