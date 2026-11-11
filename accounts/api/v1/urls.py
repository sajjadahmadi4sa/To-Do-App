from django.urls import path,include
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name='token-logout'),
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),
    path('jwt/login/', views.CustomTokenObtainPairView.as_view(), name='jwt-login'),
    path('jwt/refresh/',TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(), name='jwt_verify'),
    path('change-password/',views.ChangePasswordApiView.as_view(),name='change-password'),
    path('send_email/',views.SendEmail.as_view(),name='send-email'),
    path('activation/confirm/<str:token>/',views.ActivationAPIView.as_view(),name='activation'),
    path('activation/resend/',views.ActivationResendAPIView.as_view(),name='activation-resend'),
]
