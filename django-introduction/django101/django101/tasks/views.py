from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function based views
# function who takes at least 1 param
from django101.tasks.models import Task


#
# def home(request):
#     items = Task.objects.all()
#     item_string = ''.join(f'<li>{t.title}</li>' for t in items)
#     html = f'''
#     <h1> it works </h2>
#     <ul>
#     {item_string}
#     </ul>
#     '''
#     return HttpResponse(html)

def home(request):
    context = {
        'title': 'It works from view haha',
        'tasks': Task.objects.all()
    }
    return render(request, 'home.html', context)

# class based views
