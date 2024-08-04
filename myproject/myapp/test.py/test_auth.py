from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login(self):
        response = self.client.post('/api/login/', {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
