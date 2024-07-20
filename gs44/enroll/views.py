from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'enroll/home.html')
# def show_details(request,my_id):
#     d = {"id":my_id}
#     return render(request,'enroll/show.html',context=d)

def show_details(request,my_id):
    if my_id == 1:
        student = {'id':my_id,'name':'Aryan'}

    if my_id == 2:
        student = {'id':my_id,'name':'El Primo'}
    if my_id == 3:
        student = {'id':my_id,'name':'Mortis'}
    if my_id == 4:
        student = {'id':my_id,'name':'jessie'}

    return render(request,'enroll/show.html',context = student)
#     return render(request,'enroll/show.html',context=d)

def show_subdetails(request,my_id,my_subid):
    if my_id == 1 and my_subid == 1:
        student = {'id':my_id,'name':'Aryan'}

    if my_id == 2 and my_subid == 2:
        student = {'id':my_id,'name':'El Primo'}
    if my_id == 3 and my_subid == 3:
        student = {'id':my_id,'name':'Mortis'}
    if my_id == 4 and my_subid == 4:
        student = {'id':my_id,'name':'jessie'}

    return render(request,'enroll/show.html',context = student)