from django.shortcuts import render
def home(request):
    return render(request,"enroll/course.html")
def contact(request):
    return render(request,"enroll/contact.html")
