from django.shortcuts import render
from .forms import StudentRegistration
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
    else:
        fm = StudentRegistration()
    return render(request,'enroll/userregistration.html',{'fm':fm})
    
# Create your views here.
