from django.shortcuts import render
def getcourse1(request):
    return render(request,'course/course1.html',{
        'Title': "Django",
        'Duration':69
    })
def getcourse2(request):
    return render(request,'course/course2.html',{
   'Title':'Python',
   'Duration':420
})
# Create your views here.
