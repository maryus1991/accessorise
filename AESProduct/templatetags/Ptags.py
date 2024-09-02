from django import template

register = template.Library()


@register.filter
def tdc(value: int):
    return '{:,}'.format(value)
