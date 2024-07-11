from django.shortcuts import render
from .forms import StudentRegistration
def showformdata(request):
    fm = StudentRegistration()
    return render(request,'enroll/userregistration.html',{'fm':fm})
    
# Create your views here.
