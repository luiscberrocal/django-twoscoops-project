'''
Created on Jan 3, 2014

@author: luiscberrocal
'''
from django import template

register = template.Library()

@register.filter(name='addcss')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='add_bootstrap_behavior')
def add_bootstrap_behavior(value, placeholder, css_class='form-control'):
    return value.as_widget(attrs={'class': css_class,
                                  'placeholder' : placeholder})