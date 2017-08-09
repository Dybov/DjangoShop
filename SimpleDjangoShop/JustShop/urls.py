#!/usr/bin/env python
from django.conf.urls import url
from . import views
from .apps import JustshopConfig


app_name = JustshopConfig.name

urlpatterns = [
	url(r'^$', views.ProductList.as_view(), name = 'ProductList'),
	url(r'^category/(?P<category>[\w-]+)/$', views.ProductList.as_view(), name = 'ProductListByCategory'),
	url(r'^product/(?P<pk>\d+)/$', views.ProductDetail.as_view(), name = 'ProductDetail')
]