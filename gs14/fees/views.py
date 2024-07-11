from django.shortcuts import render
def getfees1(request):
    return render(request,'fees/fees1.html',
                  {
                      "Price":200
                  }
                  )
def getfees2(request):
    return render(request,'fees/fees2.html',
{
 "Price":400
}
)
# Create your views here.
