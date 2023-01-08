from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import views

app_name = "user"

urlpatterns = [
    path("user/register/", views.CreateUserView.as_view(), name="register"),
    path("user/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("user/refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user-address/", views.UserAddressView.as_view(), name="user-address"),
]
