from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session["name"] = "aryan"
    request.session["lname"] = "aryan2"
    return render(request,'student/setsession.html')


def getsession(request):
    name1 = request.session["name"]
    name2 = request.session["lname"]

    return render(request,'student/getsession.html',{"name1":name1,"name2":name2})


def delsession(request):
    del request.session["name"]
    return render(request,"student/delsession.html")