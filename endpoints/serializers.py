from rest_framework import serializers
from .models import TrafficInfo

class TrafficSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficInfo
        fields = '__all__'