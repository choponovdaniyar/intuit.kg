from django import template

register = template.Library()

@register.filter()
def website(text):
    return "https://intuit.kg{}".format(text)