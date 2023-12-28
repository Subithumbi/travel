from django.http import HttpResponse
from django.shortcuts import render
from .models import Places, Contributor


# Create your views here.
def demo(request):
    # name="shijin"
    obj = Places.objects.all()
    objs = Contributor.objects.all()

    return render(request, "index.html",{'result':obj,'results':objs})

# def addition(request):
#     x=int(request.GET["num1"])
#     y=int(request.GET["num2"])
#     res=x+y
#     ressub=x-y
#     return render(request,"result.html",{'result':res,'resultsub':ressub})




