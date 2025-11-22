from django.urls import path
from .views import register, add_to_list, remove_from_list, list_my_movies, login, logout_view
from .serializers import EmailTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

class EmailLoginView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer

urlpatterns = [
    path("auth/register/", register),
    path("auth/login/", login, name="login"),
    path("auth/logout/", logout_view, name="logout"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),

    path("me/list/", list_my_movies),
    path("me/list/add/<int:tmdb_id>/", add_to_list),
    path("me/list/remove/<int:tmdb_id>/", remove_from_list),
]
