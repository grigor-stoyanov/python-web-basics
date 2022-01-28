from django.urls import path

from urls_and_views.employees.views import department_details, list_departments

urlpatterns = (
    path('<id>/', department_details,name='department details'),  # prefix/ID => view
    # we can also assign the param a specific type <int: id>
    path('', list_departments)
)
