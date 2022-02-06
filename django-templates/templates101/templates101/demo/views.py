from django.shortcuts import render

# Create your views here.
from templates101.demo.models import TestModel


def home_view(request):
    context = {
        'title': 'Employee List',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam dolore esse hic impedit itaque natus unde voluptatum? Accusamus, distinctio ea, enim facere magni molestiae neque nihil quisquam tempora veritatis, voluptates?',
        'employees': [n.employees for n in TestModel.objects.all()],
        'numbers': [1,2,3,4,5,6,7,200,201,202]
    }
    return render(request, 'index.html', context)


def template_example(request):
    context = {
    }
    return render(request, 'example.html', context)
