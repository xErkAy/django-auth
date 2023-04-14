from django.test import TestCase
from django.urls import reverse
from project.models import User

class CustomTest(TestCase):
    def test_user_creation(self):
        User.objects.create_user(username='test_user', password='test_password')
        user = User.objects.get(username='test_user')
        self.assertTrue(user.check_password('test_password'))

    def test_auth(self):
        User.objects.create_user(username='test_user', password='test_password')
        data = {
            'username': 'test_user',
            'password': 'test_password'
        }
        response = self.client.post(reverse('user_auth'), data)
        self.assertEqual(response.status_code, 200)

    def test_using_header(self):
        User.objects.create_user(username='test_user', password='test_password')
        data = {
            'username': 'test_user',
            'password': 'test_password'
        }
        response = self.client.post(reverse('user_auth'), data)
        token = response.data.get('token')

        headers = {
            'Authorization': f'Bearer {token}',
        }

        response = self.client.post(reverse('test_view'), data={}, headers=headers)
        self.assertEqual(response.data.get('text'), 123)