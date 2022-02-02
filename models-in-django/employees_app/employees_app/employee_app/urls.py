from django.urls import path

from employees_app.employee_app.views import department_details, list_departments

urlpatterns = (
    path('<id>/', department_details,name='department details'),
    path('', list_departments)
)