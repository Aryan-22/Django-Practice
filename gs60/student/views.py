from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session["name"] = "aryan"
    request.session["lname"] = "tarafdar"

    return render(request,'student/setsession.html')


def getsession(request):
    name = request.session["name"]
    keys = request.session.keys()


    return render(request,'student/getsession.html',{"name":name,"keys":keys})


def delsession(request):
    request.session.flush()
    return render(request,"student/delsession.html")