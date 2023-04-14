import json

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from api.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128, min_length=4, write_only=True)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
