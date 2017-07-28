#!/usr/bin/env python
from django.conf.urls import url
from . import views
from .apps import JustshopConfig


app_name = JustshopConfig.name

urlpatterns = [
	url('^$', views.Index.as_view(), name = 'index')
]