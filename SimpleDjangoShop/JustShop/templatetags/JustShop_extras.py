# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import reverse
from django.template.library import Library
register = Library()


@register.simple_tag
def is_active_nav(request, url):
    if url == request.path :
        return "active"
    return ""