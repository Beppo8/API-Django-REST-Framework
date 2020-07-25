from rest_framework import serializers
from .models import Video
from django.contrib.auth.models User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Video
        fields = ('title', 'description')