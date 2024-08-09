from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
    request.session["name"] = "aryan"



    return render(request,'student/setsession.html')


def getsession(request):
    if "name" in request.session:
        name = request.session["name"]
        request.session.modified = True

        return render(request,'student/getsession.html',{"name":name})
    return HttpResponse("Your session has expired")

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,"student/delsession.html")