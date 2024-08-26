from rest_framework import serializers
from django.db.models import Q
from .models import FriendshipRequest, User


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email = self.validated_data['email']
        name = self.validated_data['name']

        if password != password2:
            raise serializers.ValidationError("Пароли не совпадают!")

        if User.objects.filter(Q(email=email) | Q(name=name)).exists():
            raise serializers.ValidationError(
                "Пользователь с таким email или username уже существует!")
        new_user = User(email=email, name=name)
        new_user.set_password(password)
        new_user.save()
        return new_user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
        )


class FriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = ("created_by", "created_for", "status")
