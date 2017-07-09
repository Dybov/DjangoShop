# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['publication_date', 'question_text']
	fieldsets = [
		(None,			{'fields': ['question_text']}),
		('Date info',	{'fields': ['publication_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ['question_text', 'publication_date', 'was_published_recently']
	list_filter = ['publication_date']
	search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
