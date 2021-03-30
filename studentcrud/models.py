from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    ssemester = models.IntegerField()
    semail = models.EmailField()
    scontact = models.IntegerField()


    
