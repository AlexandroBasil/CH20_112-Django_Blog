from django.contrib.auth import get_user_model
from django.http import response
from django.urls import reverse
from django.test import TestCase

from .models import Post

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.post = Post.objects.create(
            title='Test Title',
            body='Test body',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title="Sample title", body="Sample body")
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), "/posts/1/")

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "Test Title")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.body}", "Test body")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test body")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get("/posts/1/")
        no_response = self.client.get('/posts/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test Title")
        self.assertTemplateUsed(response, "post_detail.html")

    def test_post_create_view(self):
        response = self.client.post(reverse("post_new"), {
            "title": "New title",
            "body": "New body",
            "author": self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New body")

    def test_post_update_view(self):
        response = self.client.post(reverse("post_update", args="1"), {
            "title": "Updated titled",
            "body": "Updated body"
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
