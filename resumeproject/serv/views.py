from django.shortcuts import render
def services(request):
    context = {'skills':'active'}
    return render(request,'service/service.html',context)
# Create your views here.
