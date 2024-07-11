from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
from .models import User

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form validated')
            x = fm.cleaned_data["name"]
            y = fm.cleaned_data["email"]
            z = fm.cleaned_data['password']
            #reg = User(name = x,email = y,password = z)
            #reg.save()
            reg = User(id = 1)
            reg.delete()

               
    else:
        fm = StudentRegistration()
    return render(request,'enroll/userregistration.html',{'fm':fm})


# Create your views here.
