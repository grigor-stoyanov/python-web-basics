# Django uses model template view, model - db , template - presentation , view -business logic
# the view connects the info from the model and gives it to the template in required format
# url configuration contains all the path mappings in urlpatterns
# views are functions which take at least 1 parameter request
# to include multiple urls on 1 base prefix we can use include method and create our own url configuration within app
# default path converters str,int,slug(matching str to chars),path(match any non-empty str),uuid
# regex urls re_path(r'^employees/(?P<department_id>[1-5])/$',views.year_archive) u can limit the id from 1 to 5
# path('employees/<int:department_id>',views.employees_by_department_id) and the value is passed as an argument to view
# function based views and class based views
# django views must accept request as first param, returns HttpResponse!
# request holds all kinds of data we need like authentication,tokens,query params,data ect..
# django view has alot of helper functions which eliminate httpresponse
# render(),redirect(),reverse_lazy()-gives full path of url config by given name!
