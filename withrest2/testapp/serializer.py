from rest_framework import serializers

class NameSerializer(serializers.Serializer):
    #here modelserializer is not there because model is not present
    name = serializers.CharField(max_length=10)
