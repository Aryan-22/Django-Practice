from django.shortcuts import render
def project(request):
    context = {'project':'active'}
    return render(request,'edu/projects.html',context)
# Create your views here.
