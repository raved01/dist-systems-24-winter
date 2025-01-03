from rest_framework import serializers
from .models import ModelName

class ModelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelName
        fields = '__all__'  # Alle Felder des Modells werden serialisiert
