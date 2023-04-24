import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# A|add:5 --> A에다가 5를 더한다는 의미
# A|sub:5 --> A가 value 인자가 되고, 뒤에 5가 arg 인자가 된다.

@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))