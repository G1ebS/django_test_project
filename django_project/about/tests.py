from django.test import TestCase, Client


class UrlTests(TestCase):
    def test_app_homepage(self):
        response = Client().get('/about')

        self.assertEqual(
            response.status_code,
            200,
            'С базовой страницей приложения about что-то не так',
        )
