from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from sellingPortal import forms, models
# Create your views here.


def Student(request):
    students=models.Student.objects.all()
    context={'students':students}
    return render(request, 'student.html', context)
    #return HttpResponse('welcome to student page')

def Degree(request, studentId):
    degrees= models.Degree.objects.filter(studentId=studentId)
    students=models.Student.objects.get(id=studentId)
    form= forms.userDegree(request.POST or None)
    msg=''
    if form.is_valid():
        degree=models.Degree()
        degree.studentDegree=form.cleaned_data['studentDegree']
        degree.studentId= students
        degree.save()
        msg='Data is saved'
    context={'degrees':degrees,
             'form':form,
             'msg':msg
    }
    return render(request, 'degree.html', context)
    # return HttpResponse('welcome to degree page your id: '+studentId)

def Register(request):
    form= forms.userRegister(request.POST or None)
    msg=''
    if form.is_valid():
        student=models.Student()
        student.firstName=form.cleaned_data['firstName']
        student.lastName=form.cleaned_data['lastName']
        student.age=form.cleaned_data['age']
        student.birthDate=form.cleaned_data['birthDate']      
        student.save()
        msg='Data is saved'
    context={'form':form,
             'msg':msg
    }
    return render(request, 'register.html', context)



