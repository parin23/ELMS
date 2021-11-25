from django.shortcuts import render
from mysite.models import *
from django.contrib import messages

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
    colName = ["Result Id","Test ID","Course ID","Student ID","Score","Result Date","GPA / 10"]
    final = lister(showAll)
    return render(request,'index.html',{"data":final,"cols":colName})


def insertSt (request):
    if request.method == "POST" :
        if 'insert_button' in request.POST:
            saveRecord = stModel()
            saveRecord.student_id = request.POST.get('st_id')
            saveRecord.student_name = request.POST.get('st_name')
            saveRecord.save()
            messages.success(request, 'Student ID ' + saveRecord.student_id + ' is Saved Succesfully ...')
        elif 'delete_button' in request.POST:
            delObj = stModel.objects.get(student_id=request.POST.get('st_id'))
            delObj.delete()
            messages.success(request, 'Student ID ' + request.POST.get('st_id') + ' is Deleted Succesfully ...')
                    
    return render(request,'insert.html')


    
        
