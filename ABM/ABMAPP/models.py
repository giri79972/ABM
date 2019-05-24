from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    class Meta:
        abstract=True

class Emp(CommonInfo):
    sal=models.IntegerField()
    def __str__(self):
        return self.name
class Customer(CommonInfo):
    sales=models.IntegerField()
    def __str__(self):
        return self.name
class Student(CommonInfo):
    marks=models.IntegerField()
    def __str__(self):
        return self.name