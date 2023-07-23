from django import template

register = template.Library()

@register.filter
def attr(value, arg):
    attrs = arg.split(':')
    return value.as_widget(attrs={attrs[0]: attrs[1]})
