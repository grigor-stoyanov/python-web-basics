from django import template

register = template.Library()


@register.filter()
def increase_by(value, number):
    try:
        return number + value
    except TypeError:
        return int(value) + number
