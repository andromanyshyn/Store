import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
import django

django.setup()

from django.test import TestCase
from django.urls import reverse
from products.models import *


class IndexViewTest(TestCase):
    def setUp(self):
        self.path = reverse('index')

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')


class ListProductsViewTest(TestCase):
    fixtures = ['categories.json', 'products.json']

    def setUp(self):
        self.category = Categories.objects.first()
        self.products_list = Products.objects.all()[:3]
        self.products_list_by_category = Products.objects.filter(category_id=self.category.id)

    def test_view_get_products(self):
        self.path = reverse('products')
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Store - Products')
        self.assertTemplateUsed(response, 'products/products.html')

        self.assertEqual(list(response.context_data['object_list']), list(self.products_list))

    def test_view_get_products_categories(self):
        self.path = reverse('categories_products', kwargs={'category_id': self.category.id})
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Store - Products')
        self.assertTemplateUsed(response, 'products/products.html')

        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products_list_by_category)
        )






