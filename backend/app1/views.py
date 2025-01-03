from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ModelName
from .serializers import ModelNameSerializer

class ModelNameList(APIView):
    def get(self, request):
        items = ModelName.objects.all()  # Alle Daten holen
        serializer = ModelNameSerializer(items, many=True)  # Serialisieren der Daten
        return Response(serializer.data)

    def post(self, request):
        serializer = ModelNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Speichern der neuen Daten
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

