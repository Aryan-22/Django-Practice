from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form validated')
            print(fm.cleaned_data["name"])

    else:
        fm = StudentRegistration()
    return render(request,'enroll/userregistration.html',{'fm':fm})


# Create your views here.
