from django.db import models
from django.db.models import aggregates

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=150) 
    lastName= models.CharField(max_length=250)
    age= models.IntegerField(default=12)
    birthDate= models.DateTimeField()
    
    def __str__(self):
        return self.firstName

class Degree(models.Model):
    studentId=models.ForeignKey(Student, on_delete=models.CASCADE)
    studentDegree= models.CharField(max_length=250)


