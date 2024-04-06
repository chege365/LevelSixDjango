from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from lvlsix import settings
from users import views as user_views
from blog.urls import urlpatterns as blog_urlpatterns
from lvlsix.urls import urlpatterns as lvlsix_urlpatterns


class AdminUrlsTestCase(TestCase):
    def test_admin_url(self):
        url = reverse('admin:index')
        self.assertEqual(url, '/admin/')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'admin:index')


class UserUrlsTestCase(TestCase):
    def test_register_url(self):
        url = reverse('users:register')
        self.assertEqual(url, '/register/')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'users:register')

    def test_profile_url(self):
        url = reverse('users:profile')
        self.assertEqual(url, '/profile/')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'users:profile')

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'login')

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(url, '/logout/')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'logout')


class BlogUrlsTestCase(TestCase):
    def test_blog_urls(self):
        for urlpattern in blog_urlpatterns:
            url = reverse(urlpattern.name)
            resolver = resolve(url)
            self.assertEqual(resolver.view_name, urlpattern.name)


class MediaUrlsTestCase(TestCase):
    def test_media_urls(self):
        if settings.DEBUG:
            media_url = settings.MEDIA_URL
            media_root = settings.MEDIA_ROOT
            url = f'{media_url}test_image.jpg'
            self.assertEqual(url, '/media/test_image.jpg')
            resolver = resolve(url)
            self.assertEqual(resolver.view_name, 'django.views.static.serve')
            self.assertEqual(resolver.kwargs['document_root'], media_root)