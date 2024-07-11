from django.shortcuts import render
from .forms import StudentRegistration
def showformdata(request):
    fm = StudentRegistration(auto_id=True,label_suffix=" ")
    return render(request,'enroll/userregistration.html',{'fm':fm})
    
# Create your views here.
