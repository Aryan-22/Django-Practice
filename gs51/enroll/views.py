from django.shortcuts import render
from .form import SignUpForm
from django.contrib import messages


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Account created successfully")
            fm.save()

    else:
        fm = SignUpForm()


    return render(request,'enroll/signup.html',{'form':fm})