from django.contrib import admin

# Register your models here.
from employees_app.employee_app.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'company', 'job_title')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
