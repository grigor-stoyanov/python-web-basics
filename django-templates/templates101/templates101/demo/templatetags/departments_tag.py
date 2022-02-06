from django import template

from templates101.demo.models import TestModel

register = template.Library()


# miniature view with a template we assigned
@register.inclusion_tag('tags/departments_list.html')
def departments_list():
    departments = [d.department for d in TestModel.objects.all()]
    # departments = Department.objects.prefetch_related('employee_set').all()
    # departments[0].employees_set.count()
    # we return context for the template of inclusion tag
    return {
        'departments': departments
    }
