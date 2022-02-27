from django import template

from FinalPWBFeb27.main.helpers import get_profile

register = template.Library()


@register.simple_tag
def has_profile():
    if get_profile():
        return True
    return False
