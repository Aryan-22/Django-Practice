from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
def regi(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request,messages.SUCCESS,"your account has been created")

            messages.info(request,"now you can login")
            print(messages.get_level(request))
            messages.debug(request,"This is Debug")
            messages.set_level(request,messages.DEBUG)
            messages.debug(request,"This is NEW Debug")
            print(messages.get_level(request))
    else:
        fm = StudentRegistration()
    return render(request,"enroll/userregistration.html",{"fm":fm})


# Create your views here.
