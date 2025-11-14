from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name to test api"""
    name = serializers.CharField(max_length=10)
    