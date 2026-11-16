from django.test import TestCase
from datetime import datetime
from django.contrib.auth import get_user_model
from accounts.models import User

User = get_user_model()

class UserModelTest(TestCase):

    def test_create_user_with_valid_data(self):
        user = User.objects.create_user(email="user@test.com",password="Password123!")   
        self.assertEqual(user.email, "user@test.com")
        
    
        
    
