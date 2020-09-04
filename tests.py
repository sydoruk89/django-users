from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class MyTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@test.pl",
            username = "test", 
            password = "pass"
        )
    def test_user(self):
        self.assertEqual(self.user.email, 'testuser@test.pl')