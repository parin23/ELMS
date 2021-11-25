from django.shortcuts import render
from mysite.models import *

def lister(obj):# Converts the Class into a List i.e makes the table iterable as List
    obj1 = []
    for i,s in enumerate(obj):
        temp = s.__dict__
        temp =  list( temp.values() )
        temp = temp[1::]
        obj1.append(temp)
    return obj1 

def homeView(request):
    return render(request,'home.html')

def showSt (request):
    showAll = stModel.objects.all()
    colName = ["Student Id","Student Name"]
    final = lister(showAll)
    return render(request,'index.html',{"data":final,"cols":colName})

def showTeach (request):
    showAll = teachModel.objects.all()
    colName = ["Teacher Id","Teacher Name"]
    final = lister(showAll)
    return render(request,'index.html',{"data":final,"cols":colName})

def showCourseName (request):
    showAll = cnameModel.objects.all()
    colName = ["Course Id","Course Name"]
    final = lister(showAll)
    return render(request,'index.html',{"data":final,"cols":colName})


def showResultAll (request):
    showAll = resultModel.objects.all()
    colName = ["Result Id","Test ID","Course ID","Student ID","Score","Result Date","CPI"]
    final = lister(showAll)
    return render(request,'index.html',{"data":final,"cols":colName})