from django.urls import path
from .view import MyTokenObtainPairView, UserCreateAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('create-user/', UserCreateAPIView.as_view(), name='Create User'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
