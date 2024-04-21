from django.db.models import fields
from rest_framework import serializers
from .models import Clothes

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ('name', 'des', 'price', 'brand','size')