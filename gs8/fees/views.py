from django.shortcuts import render
from django.http import HttpResponse
def get_fees(request):
    return HttpResponse("g28 fees")
# Create your views here.
