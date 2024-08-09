from django.shortcuts import render

# Create your views here.
def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,"student/setcookie.html")


def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request,"student/checktestcookie.html")

def deletetestcookie(request):
    print(request.session.delete_test_cookie())
    return render(request,"student/deltestcookie.html")
