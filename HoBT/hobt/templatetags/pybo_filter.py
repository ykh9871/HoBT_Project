from django import template

register = template.Library()


# A|add:5 --> A에다가 5를 더한다는 의미
# A|sub:5 --> A가 value 인자가 되고, 뒤에 5가 arg 인자가 된다.

@register.filter
def sub(value, arg):
    return value - arg
