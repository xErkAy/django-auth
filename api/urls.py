from django.urls import path
from api.views import AuthenticationAPIView, TestAPIView, RegistrationAPIView

urlpatterns = [
    path('auth/', AuthenticationAPIView.as_view()),
    path('registration/', RegistrationAPIView.as_view()),
    path('test/', TestAPIView.as_view())
]
