from django import template

register = template.Library()


@register.filter
def tdc(value: int):
    return ('{:,}'.format(value))


@register.filter
def discount(price: int, discount: int):
    discount_price = price * (discount / 100)
    return '{:,}'.format(price - discount_price)

@register.filter
def RFS(num: int):
    return range(num)

@register.filter
def Sum(a, b):
    return '{:,}'.format(a + b)