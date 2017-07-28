# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.views.generic import ListView
from .models import Product

class Index(ListView):
	model = Product
	template_name = 'JustShop/index.django.html'

def index(request):
	return render(request,'JustShop/index.django.html')