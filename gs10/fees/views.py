from django.shortcuts import render
from django.http import HttpResponse
def get_fees(request):
    d = {'a':1,'b':2}
    return render(request,'fees/fees1.html',context=d)
# Create your views here.
