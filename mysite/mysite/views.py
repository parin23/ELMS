from django.shortcuts import render
from mysite.models import stModel

def lister(obj):
    obj1 = []
    for i,s in enumerate(obj):
        temp = s.__dict__
        temp =  list( temp.values() )
        temp = temp[1::]
        obj1.append(temp)

    return obj1

def showSt (request):
    showAll = stModel.objects.all()
    colName = ["Student Id","Student Name"]
    final = lister(showAll)
    return render(request,'index.html',{"data":final,"cols":colName})