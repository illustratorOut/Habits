from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'id_telegram',)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'id_telegram',)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_name',)
