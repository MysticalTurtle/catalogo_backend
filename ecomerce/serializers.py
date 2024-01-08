from rest_framework import serializers
from ecomerce.models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True}
        }
    def create(self, validated_data):
        # Hash de la contraseña antes de almacenarla
        user = User.objects.create_user(**validated_data)
        return user