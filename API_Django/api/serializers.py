from rest_framework import serializers
from .models import api_data

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model=api_data
        fields='__all__'