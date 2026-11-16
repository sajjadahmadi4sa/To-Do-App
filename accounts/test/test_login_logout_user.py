from django.test import TestCase
from datetime import datetime
from django.contrib.auth import get_user_model
from accounts.models import User


User = get_user_model()

class TestUserLoginLogout(TestCase):
    def test_user_login_successfully(self):
        user = User.objects.create_user(email="user@test.com",password="Password123!")
        user.is_verified = True
        user.save()
        response = self.client.post("/accounts/api/v1/token/login/",{"email": "user@test.com","password": "Password123!"})

        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)
        
    def test_user_logout_successfully(self):
        user = User.objects.create_user( email="user@test.com",password="Password123!")
        user.is_verified = True
        user.save()
        login_response = self.client.post("/accounts/api/v1/token/login/",{"email": "user@test.com","password": "Password123!"})
        token = login_response.data["token"]
        self.client.force_login(user)