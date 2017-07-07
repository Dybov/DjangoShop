# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Question, Choice


class QuestionMethodTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() should return False for questions whose
		pub_date is in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(publication_date=time)
		self.assertEqual(future_question.was_published_recently(), False)
	
	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_recently() should return True for questions whose
		pub_date is within the last day.
		"""
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(publication_date=time)
		self.assertEqual(recent_question.was_published_recently(),True)
	
	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() should return False for questions whose
		pub_date is older than 1 day.
		"""
		time = timezone.now() - datetime.timedelta(days=14)
		old_question = Question(publication_date=time)
		self.assertEqual(old_question.was_published_recently(), False)


def create_question_without_any_choice(question_text, days):
	"""
	Creates a question with the given `question_text` published the given
	number of `days` offset to now (negative for questions published
	in the past, positive for questions that have yet to be published).
	"""
	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text,
								   publication_date = time)

def create_question_with_choices(question_text, days, choice_text="Some choice"):
	question = create_question_without_any_choice(question_text, days)
	return question, Choice.objects.create(question=question,choice_text=choice_text)
	
	

class QuestionIndexViewTests(TestCase):
	def test_index_view_with_no_question(self):
		"""
		If no questions exist, an appropriate message should be displayed.
		"""
		response = self.client.get(reverse('Polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available")
		self.assertQuerysetEqual(response.context['latest_question_list'],[])
	
	def test_index_view_with_a_past_question(self):
		"""
		Questions with a pub_date in the past should be displayed on the
		index page.
		"""
		create_question_with_choices(question_text='Past question', days=-30)
		response = self.client.get(reverse('Polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],
								 ['<Question: Past question>'])
	
	def test_index_view_with_a_future_question(self):
		"""
		Questions with a pub_date in the future should not be displayed on
		the index page.
		"""
		create_question_with_choices(question_text='Future question', days=30)
		response = self.client.get(reverse('Polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], [])
	
	def test_index_view_with_old_question_and_future_question(self):
		"""
		Even if both past and future questions exist, only past questions
		should be displayed.
		"""
		create_question_with_choices(question_text='Past question', days=-30)
		create_question_with_choices(question_text='Future question', days=30)
		response = self.client.get(reverse('Polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],
								 ['<Question: Past question>'])
	
	def	test_index_view_with_two_old_questions(self):
		"""
		The questions index page may display multiple questions.
		"""
		create_question_with_choices(question_text='Past question 1', days=-30)
		create_question_with_choices(question_text='Past question 2', days=-10)
		response = self.client.get(reverse('Polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],
			['<Question: Past question 2>', '<Question: Past question 1>']
		)
	
	def test_index_view_with_question_without_choice(self):
		"""
		The questions index page must not display question without any choice
		"""
		create_question_without_any_choice(question_text='Past question 1', days=0)
		response = self.client.get(reverse('Polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],[])
		
	def test_index_view_with_question_with_and_without_choice(self):
		"""
		The questions index page must not display question without any choice, but display questions with atleast choice
		"""
		create_question_with_choices(question_text='Question with choice', days=0)
		create_question_without_any_choice(question_text='Question without choice', days=0)
		response = self.client.get(reverse('Polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Question with choice>'])

class QuestionDetailViewTests(TestCase):
	def test_detail_view_with_a_future_question(self):
		"""
		The detail view of a question with a pub_date in the future should
		return a 404 not found.
		"""
		future_question = create_question_without_any_choice(question_text = 'Future question', days=30)
		response = self.client.get(reverse('Polls:detail',
										   kwargs={'pk':future_question.id}))
		self.assertEqual(response.status_code, 404)
	
	def test_detail_view_with_a_past_question(self):
		"""
		The detail view of a question with a pub_date in the past should
		display the question's text.
		"""
		past_question = create_question_without_any_choice(question_text = 'Old question', days=-1)
		response = self.client.get(reverse('Polls:detail',
										   kwargs={'pk':past_question.id}))
		self.assertContains(response, past_question.question_text)