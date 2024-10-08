from django.shortcuts import render
from .forms import StudentRegistration,TeacherRegistration

def student_form(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = StudentRegistration()
    return render(request,"enroll/student.html",{"fm":fm})
 
def teacher_form(request):
    if request.method == "POST":
        fm = TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = TeacherRegistration()
    return render(request,"enroll/teacher.html",{"fm":fm})



# Create your views here.
