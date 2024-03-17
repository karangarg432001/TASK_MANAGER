from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        is_staff = validated_data.pop('is_staff', False)
        is_superuser = validated_data.pop('is_superuser', False)
        user = User.objects.create_user(**validated_data)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True},
                        'is_staff': {'write_only': True},
                        'is_superuser': {'write_only': True}
                    }

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
