import os

from django.urls import reverse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
import django

django.setup()

from django.test import TestCase
from .models import *


class RegistrationViewTest(TestCase):
    def setUp(self):
        self.path = reverse('registration')
        self.correct_data = {
            'first_name': 'andrew',
            'last_name': 'rshyn',
            'username': 'andrewr',
            'email': 'oigeorgn@gmail.com',
            'password1': 'a9517535',
            'password2': 'a9517535',
        }
        self.incorrect_data = {
            'first_name': 'andrew',
            'last_name': 'rshyn',
            'username': 'andrewr',
            'email': 'oigeorgn@gmail.com',
            'password1': 'a9517535',
            'password2': '1234567',
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Store - Registration')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post(self):
        response = self.client.post(self.path, self.correct_data)

        self.assertEqual(response.status_code, 302)


class UserLoginViewTest(TestCase):
    def setUp(self):
        self.path = reverse('login')
        self.data = {
            'username': 'valera',
            'password': 'a9517535',
        }

    def test_user_login_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Store - Login')
        self.assertTemplateUsed(response, 'users/login.html')

    def test_user_login_post(self):
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, 200)


class ProfileViewTest(TestCase):
    def setUp(self):
        user = User.objects.first()
        self.path = reverse('profile', kwargs={'pk': user.id})

    def test_user_profile_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)

