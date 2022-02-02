import random
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from employees_app.employee_app.models import Department, Employee
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView


# black magic
class HomeView(TemplateView):
    template_name = 'index.html'


def home(request):
    rand_number = random.randint(0, 1024)
    print(reverse_lazy('department details', kwargs={'id': 1}))
    return render(request, 'index.html', context={'number': rand_number, })


def redirect_to_home(request):
    return redirect(to='home')


def redirect_to_random_department(request):
    return redirect(to='department details', id=random.randint(1, 1024))


# return HttpResponseRedirect()

def notFound(request):
    # return HttpResponseNotFound()
    raise Http404()


# def home(request):
#     html = f'<h1>{request.method}: This is home!</h1>'
#     if request.method == 'GET':
#         return HttpResponse(html,
#                             status=201,
#                             # content_type='text/plain',
#                             headers={'X-Header': 'Django'})
#     else:
#         return HttpResponse(html)


def department_details(request, id):
    if not isinstance(id, int):
        # return 404
        pass
    return HttpResponse(f'This is department {id}')


def list_departments(request):
    # creating departments v1
    department = Department(
        # must type params explicitly!
        name=f"New Department{random.randint(1, 1024)}",
    )
    department.save()
    # v2 without save
    Department.objects.create(
        name=f'New Department {random.randint(1,1024)}'
    )
    # if we change the pk we create anotther object!

    # objects.get() must alwayss return a single value!

    context = {
        # objects is an sql query manager
        'departments': Department.objects
            .prefetch_related('employee_set')
            .all(),
        # 'departments':Department.objects.filter(name__endswith='app'),
        'employees': Employee.objects.all()

    }
    return render(request, 'list_departments.html', context)


def list_employees(request):
    return HttpResponse('')
