from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

def showformdata(request):
    if request.method == 'POST':
        pi = User.objects.get(pk= 1)


        fm = StudentRegistration(request.POST,instance = pi)
        if fm.is_valid():
            
            print('Form validated')
            # x = fm.cleaned_data["name"]
            # y = fm.cleaned_data["email"]
            # z = fm.cleaned_data['password']
            # reg = User(name = x,email = y,password = z)
            # reg.save()
            fm.save()


               
    else:
        fm = StudentRegistration()

    
    return render(request,'enroll/userregistration.html',{'fm':fm})


# Create your views here.
