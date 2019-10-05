from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import RegisterView

app_name = 'accounts'

urlpatterns = [
    path('auth-token/', obtain_jwt_token, name='login'),
    path('refresh-token/', refresh_jwt_token, name='refresh_token'),
    path('verify-token/', verify_jwt_token, name='verify_token'),
    path('signup/', RegisterView.as_view(), name="signup")
]
