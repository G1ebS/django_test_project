from django.test import TestCase, Client


class UrlTests(TestCase):
    def test_app_homepage(self):
        response = Client().get('/')

        self.assertEqual(response.status_code, 200)
