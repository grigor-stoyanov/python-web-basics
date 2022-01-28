import random
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

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
    return HttpResponse('List of Departments')


def list_employees(request):
    return HttpResponse('')
