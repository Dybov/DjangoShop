# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category

class ProductList(ListView):
	model = Product
	template_name = 'JustShop/index.django.html'
	context_object_name = 'products'
	def get_queryset(self):
		objects = self.model.objects.all()
		self.category_slug = self.kwargs.get('category')
		if self.category_slug:
			cat =  get_object_or_404(Category, category_slug = self.category_slug)
			return objects.filter(category=cat)
		return objects
	def get_context_data(self, **kwargs):
		context = super(ProductList, self).get_context_data(**kwargs)
		if self.category_slug:
			context['category'] = self.category_slug
		return context

class ProductDetail(DetailView):
	model = Product
	template_name = 'JustShop/detail.django.html'
	context_object_name = 'product'
	def get_queryset(self):
		return Product.objects.filter(available=True)
