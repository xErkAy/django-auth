from django.urls import path
from api.views import AuthenticationAPIView, TestAPIView, RegistrationAPIView

urlpatterns = [
    path('auth/', AuthenticationAPIView.as_view(), name='user_auth'),
    path('registration/', RegistrationAPIView.as_view(), name='user_register'),
    path('test/', TestAPIView.as_view(), name='test_view')
]
