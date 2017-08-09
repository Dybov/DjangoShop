# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category

class ProductList(ListView):
	model = Product
	template_name = 'JustShop/index.django.html'
	context_object_name = 'products'
	
	def get_context_data(self, **kwargs):
		context = super(ProductList, self).get_context_data(**kwargs)
		category_slug = self.kwargs.get('category')
		if category_slug:
			category = get_object_or_404(Category, category_slug = category_slug)
			context[self.context_object_name] = \
				context[self.context_object_name].filter(category=category)
			context['category'] = category
		context['categories'] = Category.objects.all()
		return context

class ProductDetail(DetailView):
	model = Product
	template_name = 'JustShop/detail.django.html'
	context_object_name = 'product'
	def get_queryset(self):
		return Product.objects.filter(available=True)
