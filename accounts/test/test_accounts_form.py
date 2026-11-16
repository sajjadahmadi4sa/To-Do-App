from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.forms import RegisterForm


class RegisterFormTest(TestCase):

    def test_valid_register_form(self):
        form = RegisterForm(data={
            "email": "user@test.com",
            "password": "StrongPassword123!",
            "password2": "StrongPassword123!"})
        self.assertTrue(form.is_valid())


    def test_register_form_invalid_email(self):
        form = RegisterForm(data={
            "email": "invalid-email",
            "password": "StrongPassword123!",
            "password2": "StrongPassword123!"})
        self.assertFalse(form.is_valid())