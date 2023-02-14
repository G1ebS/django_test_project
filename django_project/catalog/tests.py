from django.test import TestCase, Client


class UrlTests(TestCase):
    def test_app_homepage(self):
        response = Client().get('catalog/')

        self.assertEqual(
            response.status_code,
            200,
            'С домашней страницей приложения catalog что-то не так',
        )

    def test_app_page_item_detail(self):
        response = Client().get('/catalog/1/')
        self.assertEqual(
            response.status_code,
            200,
            'Со страницей, с информацией о товаре что-то не так',
        )
