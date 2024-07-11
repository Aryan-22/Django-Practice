from django.shortcuts import render
from django.http import HttpResponse

def lp(request):
    return HttpResponse("Hello gs4")

def calc(request):
    a = 10 + 10
    return HttpResponse(a)



# Create your views here.
