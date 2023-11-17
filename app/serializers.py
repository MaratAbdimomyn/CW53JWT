from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']