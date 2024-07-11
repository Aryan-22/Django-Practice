from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    a = 10 + 10
    return HttpResponse(a)
def index(request):
    return HttpResponse("<h1>This is Home Page</h1>")

def test(request):
    return HttpResponse("Hi my name is aryan")
