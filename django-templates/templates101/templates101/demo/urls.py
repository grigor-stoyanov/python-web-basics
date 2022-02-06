from django.urls import path

from templates101.demo.views import home_view, template_example

urlpatterns = [
    path('home/', home_view, name='go to home'),
    path('template/', template_example, name='go to example')
]
