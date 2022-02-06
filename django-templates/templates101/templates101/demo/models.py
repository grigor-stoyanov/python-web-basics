from django.db import models


# Create your models here.
class TestModel(models.Model):
    employees = models.CharField(max_length=40, null=True, blank=True)
    department = models.CharField(max_length=40,null=True,blank=True,default='1')