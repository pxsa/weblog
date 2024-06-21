from django.test import TestCase

from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Post

# Create your tests here.
class BlogPostTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.user = User.objects.create(username='user1')
		cls.post = Post.objects.create(
					title = 'post1',
					text = 'some text for description',
					status = Post.STATUS_CHOICES[0][0],
					author = cls.user,
				)

		cls.post_draft = Post.objects.create(
				title = 'post2',
				text = 'some text',
				status = Post.STATUS_CHOICES[1][0],
				author = cls.user,
			)

	# def setUp(self):
	# 	pass


	def test_all_by_url(self):
		response = self.client.get('/blog/')
		self.assertEqual(response.status_code, 200)

	def test_all_by_name(self):
		response = self.client.get(reverse('all_posts'))
		self.assertEqual(response.status_code, 200)

	def test_post_title(self):
		response = self.client.get(reverse('all_posts'))
		self.assertContains(response, self.post.title)

	def test_post_details(self):
		response = self.client.get(reverse('post_detail', args=[self.post.id]))
		self.assertContains(response, self.post.title)
		self.assertContains(response, self.post.text)
		# self.assertContains(response, self.post.date_created)
		# self.assertContains(response, self.post.author.username)

	def test_post_detail_404(self):
		response = self.client.get(reverse('post_detail', args=[999]))
		self.assertEqual(response.status_code, 404)


	def test_draft_post(self):
		response = self.client.get(reverse('all_posts'))
		# post 1 -> published
		self.assertContains(response, self.post.title)
		# post 2 -> draft
		self.assertNotContains(response, self.post_draft.title)


	def test_create_post(self):
		response = self.client.post(reverse('create_post'), {
				'title': 'some title',
				'text': 'some text',
				'status': Post.STATUS_CHOICES[0][0],
				'author': self.user.id,
			})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(Post.objects.last().title, 'some title')
		self.assertEqual(Post.objects.last().text, 'some text')

	def test_update_post(self):
		response = self.client.post(reverse('update_post', args=[self.post_draft.id]), {
				'title': 'Post1 Updated',
				'text': 'This text is Updated',
				'status': Post.STATUS_CHOICES[0][0],
				'author': self.user.id,
			})

		self.assertEqual(response.status_code, 302)
		self.assertEqual(Post.objects.last().title, 'Post1 Updated')
		self.assertEqual(Post.objects.last().text, 'This text is Updated')


	def test_remove_post(self):
		response = self.client.post(reverse('remove_post', args=[self.post.id]))
		self.assertEqual(response.status_code, 302)
