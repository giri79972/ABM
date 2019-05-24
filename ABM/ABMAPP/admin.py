from django.contrib import admin
from .models import Emp,Customer,Student

# Register your models here.

class AdminEmp(admin.ModelAdmin):
    list_display=['name','loc','sal']
class AdminCustomer(admin.ModelAdmin):
    list_display=['name','loc','sales']
class AdminStudent(admin.ModelAdmin):
    list_display=['name','loc','marks']

admin.site.register(Emp,AdminEmp)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Student,AdminStudent)