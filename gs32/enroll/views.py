from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect

def thankyou(request):
    return render(request,"enroll/success.html")
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            password = fm.cleaned_data["password"]
            print(name)
            print(email)
            print(password)
           # return render(request,'enroll/success.html',{'fm':fm})
            return HttpResponseRedirect("/reg/success")
    else:
        fm = StudentRegistration()
    return render(request,'enroll/userregistration.html',{'fm':fm})


# Create your views here.
