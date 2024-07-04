from django.contrib import admin
from Emp_Info.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')

admin.site.register(Employee, EmployeeAdmin)

