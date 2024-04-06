from django.test import TestCase
from django.conf import settings


class SettingsTestCase(TestCase):
    def test_secret_key(self):
        self.assertIsNotNone(settings.SECRET_KEY)

    def test_debug_mode(self):
        self.assertTrue(settings.DEBUG)

    def test_allowed_hosts(self):
        self.assertGreater(len(settings.ALLOWED_HOSTS), 0)

    def test_installed_apps(self):
        self.assertIn('blog.apps.BlogConfig', settings.INSTALLED_APPS)
        self.assertIn('users.apps.UsersConfig', settings.INSTALLED_APPS)
        self.assertIn('crispy_forms', settings.INSTALLED_APPS)
        self.assertIn('crispy_bootstrap4', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.admin', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.auth', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.contenttypes', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.sessions', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.messages', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.staticfiles', settings.INSTALLED_APPS)

    def test_database_settings(self):
        self.assertEqual(settings.DATABASES['default']['ENGINE'], 'django.db.backends.sqlite3')
        self.assertIsNotNone(settings.DATABASES['default']['NAME'])

    def test_static_files_settings(self):
        self.assertEqual(settings.STATIC_URL, '/static/')
        self.assertIsNotNone(settings.MEDIA_ROOT)
        self.assertEqual(settings.MEDIA_URL, '/media/')

    def test_crispy_settings(self):
        self.assertEqual(settings.CRISPY_ALLOWED_TEMPLATE_PACKS, 'bootstrap4')
        self.assertEqual(settings.CRISPY_TEMPLATE_PACK, 'bootstrap4')

    def test_login_redirect_url(self):
        self.assertEqual(settings.LOGIN_REDIRECT_URL, 'blog-home')

    def test_login_url(self):
        self.assertEqual(settings.LOGIN_URL, 'login')

    def test_allowed_hosts(self):
        self.assertIn('127.0.0.1', settings.ALLOWED_HOSTS)
        self.assertIn('127.0.0.1:8000', settings.ALLOWED_HOSTS)
        self.assertIn('employee-dev.azurewebsites.net', settings.ALLOWED_HOSTS)
        self.assertIn('www.employee-dev.azurewebsites.net', settings.ALLOWED_HOSTS)
        self.assertIn('employeeblog.azurewebsites.net', settings.ALLOWED_HOSTS)