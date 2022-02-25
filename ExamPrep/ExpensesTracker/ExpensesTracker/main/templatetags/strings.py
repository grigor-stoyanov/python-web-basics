from django import template

register = template.Library()


@register.simple_tag()
def full_name(profile):
    return f'{profile.first_name} {profile.last_name}'
