from django import template

register=template.Library()


@register.filter(name='swapping')
def swapping(value):
    return value.swapcase()

@register.filter()
def upper(value):
    return value.upper()

@register.filter()
def lower(value):
    return value.lower()

@register.filter()
def count(value,arg):
    return value.count(arg)

@register.filter()
def counting(value,arg):
    c=0
    for a in range(len(value)):
        if value[a:a+len(arg)]==arg:
            c+=1
    return c

@register.filter()
def remove(value,arg):
    return value.replace(arg,'')


#register.filter('swapping',swapping)
#register.filter('upper',upper)
#register.filter('lower',lower)
#register.filter('count',count)
#register.filter('counting',counting)
#register.filter('remove',remove)

