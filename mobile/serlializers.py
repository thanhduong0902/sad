from django.db.models import fields
from rest_framework import serializers
from .models import Mobile

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('brand', 'des', 'name', 'price')