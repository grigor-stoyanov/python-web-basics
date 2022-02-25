from django import template
from django.db.models import Sum

from ExpensesTracker.main.models import Expense, Profile

register = template.Library()


@register.simple_tag()
def count_leftover():
    expenses = Expense.objects.aggregate(Sum('price'))
    budget = Profile.objects.all()[0].budget
    return f'{budget - expenses["price__sum"]:.2f}' if expenses['price__sum'] else budget

@register.simple_tag()
def count_items_bought():
    return Expense.objects.all().count()