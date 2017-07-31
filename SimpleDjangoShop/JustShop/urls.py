#!/usr/bin/env python
from django.conf.urls import url
from . import views
from .apps import JustshopConfig


app_name = JustshopConfig.name

urlpatterns = [
	url(r'^$|^category/(?P<category>[\w-]+)/$', views.ProductList.as_view(), name = 'ProductList'),
	url(r'^product/(?P<slug>[\w-]+)/(?P<pk>\d+)/$', views.ProductDetail.as_view(), name = 'ProductDetail')
]