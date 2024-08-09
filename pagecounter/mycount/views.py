from django.shortcuts import render

def home(request):
    cnt = request.session.get('count',0)
    cnt += 1

    request.session['count'] = cnt
    return render(request,'mycount/home.html',{"count":cnt})

# Create your views here.
