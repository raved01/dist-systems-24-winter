from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShoppingItem
from .serializers import ShoppingItemSerializer

class ShoppingItemList(APIView):
    def get(self, request):
        items = ShoppingItem.objects.all()
        serializer = ShoppingItemSerializer(items, many=True)
        return Response(serializer.data)

class ShoppingItemDetail(APIView):
    def get(self, request, name):
        try:
            item = ShoppingItem.objects.get(name=name)
        except ShoppingItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ShoppingItemSerializer(item)
        return Response(serializer.data)

class ShoppingItemCreate(APIView):
    def post(self, request):
        serializer = ShoppingItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShoppingItemUpdate(APIView):
    def put(self, request, name):
        try:
            item = ShoppingItem.objects.get(name=name)
        except ShoppingItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ShoppingItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShoppingItemDelete(APIView):
    def delete(self, request, name):
        try:
            item = ShoppingItem.objects.get(name=name)
        except ShoppingItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


