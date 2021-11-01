import re 
from django import template 

register = template.Library()

@register.filter(name='single_exclamation')
def single_exclamation(value, args):
    pattern = '[!]{'+str(args-1)+'}[!]+'
    return re.sub(pattern, '!'*args, value)