from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import UserMovie
from .serializers import RegisterSerializer, UserMovieSerializer
from .services import TMDBService
from rest_framework_simplejwt.tokens import RefreshToken


# -------------------------
# AUTH
# -------------------------
@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        return Response({"success": True, "user_id": user.id}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(request, username=email, password=password)
    if user is None:
        return Response({"detail": "Email ou senha incorretos."}, status=400)

    refresh = RefreshToken.for_user(user)

    return Response({
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "user_id": user.id
    })
    

# -------------------------
# FILMES
# -------------------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_list(request, tmdb_id):
    if UserMovie.objects.filter(user=request.user, tmdb_id=tmdb_id).exists():
        return Response({"detail": "Filme já está na lista."}, status=400)

    data = TMDBService.fetch_movie(tmdb_id)

    movie = UserMovie.objects.create(
        user=request.user,
        tmdb_id=tmdb_id,
        title=data["title"],
        poster_path=data.get("poster_path"),
        overview=data.get("overview"),
        release_date=data.get("release_date")
    )

    return Response(UserMovieSerializer(movie).data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def remove_from_list(request, tmdb_id):
    deleted, _ = UserMovie.objects.filter(user=request.user, tmdb_id=tmdb_id).delete()
    return Response({"removed": deleted > 0})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_my_movies(request):
    movies = UserMovie.objects.filter(user=request.user)
    return Response(UserMovieSerializer(movies, many=True).data)
