from django.db import models


# Create your models here.
class EmployeeModel(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=40)
    esal = models.FloatField()
    eaddress = models.CharField(max_length=200)
