from django.test import SimpleTestCase, TestCase
from django.test.client import Client
from django.urls import reverse, resolve
from blog.views import (
    SeasonListView, SeasonCreateView, SeasonDetailView,
    SpotifyApiView, AddPlaylistView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    ReplyCreateView
)


class TestUrls(SimpleTestCase):

    def test_homepage_url_resolves(self):
        url = reverse('homepage')
        self.assertEqual(resolve(url).func.view_class, SeasonListView)

    def test_create_season_url_resolves(self):
        url = reverse('create_season')
        self.assertEqual(resolve(url).func.view_class, SeasonCreateView)

    def test_season_detail_url_resolves(self):
        url = reverse('season_detail', args=['test-slug'])
        self.assertEqual(resolve(url).func.view_class, SeasonDetailView)

    def test_spotify_search_url_resolves(self):
        url = reverse('spotify_search', args=['test-slug'])
        self.assertEqual(resolve(url).func.view_class, SpotifyApiView)

    def test_add_playlist_url_resolves(self):
        url = reverse('add_playlist', args=['test-slug'])
        self.assertEqual(resolve(url).func.view_class, AddPlaylistView)

    def test_season_comment_url_resolves(self):
        url = reverse('season_comment', args=['test-slug'])
        self.assertEqual(resolve(url).func.view_class, CommentCreateView)

    def test_comment_reply_url_resolves(self):
        url = reverse('comment_reply', args=['test-slug', '1'])
        self.assertEqual(resolve(url).func.view_class, ReplyCreateView)

    def test_update_comment_url_resolves(self):
        url = reverse('update_comment', args=['test-slug', '1'])
        self.assertEqual(resolve(url).func.view_class, CommentUpdateView)

    def test_delete_comment_url_resolves(self):
        url = reverse('delete_comment', args=['test-slug', '1'])
        self.assertEqual(resolve(url).func.view_class, CommentDeleteView)


class TestLoginRequired(TestCase):

    def setUp(self):
        self.client = Client()

    def test_season_comment_url_login_required_decorator(self):
        url = reverse('season_comment', kwargs={'slug': 'test-slug'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_comment_reply_url_login_required_decorator(self):
        url = reverse('comment_reply', kwargs={'slug': 'test-slug', 'id': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_update_comment_url_login_required_decorator(self):
        url = reverse('update_comment', kwargs={'slug': 'test-slug', 'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_delete_comment_url_login_required_decorator(self):
        url = reverse('delete_comment', kwargs={'slug': 'test-slug', 'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={url}')
