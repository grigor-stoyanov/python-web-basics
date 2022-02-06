from django import template

# we create a register giving our decorators
register = template.Library()


# our custom filter
@register.filter()
def capitalise(value):
    """
    Capitalises the value, i.e. makes first letter capital an lowers rest
    THis IS tEXt => This is text
    :param value: string
    :return: string
    """
    value = str(value)
    return value[0].upper() + value[1:].lower()

@register.filter()
def do_nothing(value):
    return value