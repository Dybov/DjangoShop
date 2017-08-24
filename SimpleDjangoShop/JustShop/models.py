# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.db import models
from django.core.validators import MinValueValidator
from django.shortcuts import reverse
from .apps import JustshopConfig

app_name = JustshopConfig.name

class Category(models.Model):
	"""Category class for marking products"""
	name = models.CharField(max_length = 127, verbose_name = _('Имя категории'))
	slug = models.SlugField(max_length = 127, allow_unicode = True , verbose_name = _('Краткое имя'))

	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.__unicode__()
	def get_absolute_url(self):
		return reverse('%s:ProductListByCategory' % app_name,
					   kwargs = {'category':self.slug}
					   )
	class Meta:
		ordering = ['name']
		verbose_name_plural = _('categories')

class Product(models.Model):
	"""Product itself"""
	category = models.ForeignKey(
		Category,
		on_delete = models.PROTECT, #It raises exception when smbd try to delete joined category
	)
	name = models.CharField(max_length = 127, verbose_name = _('Название'))
	slug = models.SlugField(max_length = 127, allow_unicode = True, verbose_name = _('Краткое название товара'))
	image = models.ImageField(upload_to = 'products/%Y/%m/%d', blank = True, verbose_name = _('Изображение товара'))
	description = models.TextField(blank=True, verbose_name = _('Описание'))
	price = models.DecimalField(decimal_places = 2,
								max_digits = 6,
								verbose_name = _('Цена, рубль'),
								validators=[
									MinValueValidator(0.01)],
	)
	stock = models.PositiveIntegerField(verbose_name = _('На складе'))
	available = models.BooleanField(default = True, verbose_name = _('Доступен'))
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.slug
	def __str__(self):
		return self.__unicode__()
	def get_absolute_url(self):
		return reverse('%s:ProductDetail' % app_name,
					   kwargs = {'pk':self.pk}
					   )
