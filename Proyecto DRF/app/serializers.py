from rest_framework import serializers
from .models import User,Role
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'dni', 'birth_date', 'role', 'activo']

class RoleSerializer(serializers.ModelSerializer):

    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'users']