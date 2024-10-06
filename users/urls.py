from django.urls import path

from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserCreateAPIview

app_name = UsersConfig.name

urlpatterns = [
    path('registrate/', UserCreateAPIview.as_view(), name='registrate_user'),
    path('obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]