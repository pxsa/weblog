from django.test import TestCase

from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Post

# Create your tests here.
class BlogPostTest(TestCase):
	def setUp(self):
		self.user = User.objects.create(username='user1')
		self.post = Post.objects.create(
					title = 'post1',
					text = 'some text for description',
					status = Post.STATUS_CHOICES[0],
					author = self.user,
				)

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
