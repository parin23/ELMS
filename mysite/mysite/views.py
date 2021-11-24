from django.shortcuts import render
from mysite.models import stModel

def showSt (request):
    showAll = stModel.objects.all()
    return render(request,'index.html',{"data":showAll})