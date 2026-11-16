from django.test import TestCase
from django.urls import reverse, resolve
from accounts.api.v1.views import (
    RegistrationApiView,
    CustomObtainAuthToken,
    CustomDiscardAuthToken,
    CustomTokenObtainPairView,
    ChangePasswordApiView,
    ResetPasswordEmailApiView,
    ResetPasswordApiView,
    SendEmail,
    ActivationAPIView,
    ActivationResendAPIView
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


class AccountsUrlTest(TestCase):

    def test_registration_url_resolve(self):
        url = reverse('registration')
        self.assertEqual(resolve(url).func.view_class, RegistrationApiView)

    def test_token_login_url_resolve(self):
        url = reverse('token-login')
        self.assertEqual(resolve(url).func.view_class, CustomObtainAuthToken)

    def test_token_logout_url_resolve(self):
        url = reverse('token-logout')
        self.assertEqual(resolve(url).func.view_class, CustomDiscardAuthToken)

    def test_jwt_login_url_resolve(self):
        url = reverse('jwt-login')
        self.assertEqual(resolve(url).func.view_class, CustomTokenObtainPairView)

    def test_jwt_refresh_url_resolve(self):
        url = reverse('jwt_refresh')
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)

    def test_jwt_verify_url_resolve(self):
        url = reverse('jwt_verify')
        self.assertEqual(resolve(url).func.view_class, TokenVerifyView)

    def test_change_password_url_resolve(self):
        url = reverse('change-password')
        self.assertEqual(resolve(url).func.view_class, ChangePasswordApiView)

    def test_reset_password_url_resolve(self):
        url = reverse('reset-password')
        self.assertEqual(resolve(url).func.view_class, ResetPasswordEmailApiView)

    def test_reset_password_confirm_url_resolve(self):
        url = reverse('reset-password-confirm',args=['test_uid', 'test_token'])
        self.assertEqual(resolve(url).func.view_class, ResetPasswordApiView)

    def test_send_email_url_resolve(self):
        url = reverse('send-email')
        self.assertEqual(resolve(url).func.view_class, SendEmail)

    def test_activation_url_resolve(self):
        url = reverse('activation', args=['test-token'])
        self.assertEqual(resolve(url).func.view_class, ActivationAPIView)

    def test_activation_resend_url_resolve(self):
        url = reverse('activation-resend')
        self.assertEqual(resolve(url).func.view_class, ActivationResendAPIView)