# model allows us to work with db using python code trough ORM(object relational mapping)
# Django automatically creates required queries and executes them
# It's good to configure logging to watch all sql queries made by the app
# to execute and make sql queries django uses commands make migrations and migrate
# ensure to add installed apps into settings before attempting to migrate!
# also, configurate database settings from DATABASE
# model conventions: fields should be class attributes, with no more than 1 underscore
# fields can be CharField(with max length),TextField(large text),
# IntegerField,PositiveIntegerField,FloatField(saving as negative steps of 2),
# DecimalField(max_digits,decimal_p) for exact values saved as 2 ints
# DateField,TimeField,DateTimeField,(auto_now - updated,auto_now_add - not updated)
# BooleanField,UrlField,EmailField,
# inpectdb command allows us to copy models into python code from a db
# options: null - can store empty values,blank(validation related) empty string is not none!
# ,default(placeholder),unique
# primary_key is usually added by default in django,choice((list of tuples with 2 values))
# verbose_name how you want the default label to look visually
# many to many connection tables can be defined on their own or created by default
# we can insert class Meta for additional information inside our model
# i.e. how to sort the data,weather model is abstract,
# built in model methods __str__() changes default name of model e.g. department(object)1
# get_absolute_url() returns url of application
# all sql queries accessed trough view are done trough the objects object
# Migrations are dependant on eachother they give representation of the structure of the table in code
# migrations are reversable
