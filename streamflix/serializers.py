from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserMovie
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=4)

    class Meta:
        model = User
        fields = ["id", "email", "password"]

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        return user


class UserMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovie
        fields = "__all__"
        read_only_fields = ("user", "added_at")

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email:
            raise serializers.ValidationError("O campo email é obrigatório")

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("Usuário não encontrado")
        
        if not password:
            raise serializers.ValidationError("Senha obrigatória")

        attrs["username"] = user.username
        return super().validate(attrs)

