# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import reverse
from django.template.library import Library
from django.urls import resolve
register = Library()

def app_name(url):
    return resolve(url).app_name

@register.simple_tag(takes_context=True)
def is_active_nav(context, url):
    if url == context["request"].path :
        return " active"
    return ""

@register.simple_tag(takes_context=True)
def get_current_app_name(context):
    return app_name(context['request'].path)

@register.simple_tag(takes_context=True)
def is_active_app(context, app_name):
    if get_current_app_name(context) == app_name:
        return " active"
    return ""