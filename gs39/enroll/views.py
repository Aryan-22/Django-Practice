from django.shortcuts import render
from .forms import StudentRegistration


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():

            print('Form validated')
            x = fm.cleaned_data["name"]
            y = fm.cleaned_data["email"]
            z = fm.cleaned_data['password']
            print(x)
            print(y)
            print(z)
               
    else:
        fm = StudentRegistration()

    
    return render(request,'enroll/userregistration.html',{'fm':fm})


# Create your views here.
