from django.contrib import admin

# Register your models here.
from django101.tasks.models import Task


# version 1
# admin.site.register(Task)

# version 2 allows extensibility
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    sortable_by = ('title',)