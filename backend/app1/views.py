from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShoppingItem
from .serializers import ShoppingItemSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ShoppingItemList(APIView):
    http_method_names = ['get', 'post']

    @swagger_auto_schema(
        operation_description="Get all shopping items",
        responses={200: ShoppingItemSerializer(many=True)}
    )
    def get(self, request):
        items = ShoppingItem.objects.all()
        serializer = ShoppingItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new shopping item",
        request_body=ShoppingItemSerializer,
        responses={
            201: ShoppingItemSerializer,
            400: "Bad Request"
        }
    )
    def post(self, request):
        serializer = ShoppingItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShoppingItemEdit(APIView):
    http_method_names = ['get', 'put', 'delete']
    @swagger_auto_schema(
        operation_description="Get a specific shopping item by name",
        manual_parameters=[
            openapi.Parameter(
                'name',
                openapi.IN_PATH,
                description="Name of the shopping item",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: ShoppingItemSerializer,
            404: "Not Found"
        }
    )
    def get(self, request, name):
        try:
            item = ShoppingItem.objects.get(name=name)
        except ShoppingItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ShoppingItemSerializer(item)
        return Response(serializer.data)
    @swagger_auto_schema(
        operation_description="Update a shopping item",
        request_body=ShoppingItemSerializer,
        manual_parameters=[
            openapi.Parameter(
                'name',
                openapi.IN_PATH,
                description="Name of the shopping item to update",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: ShoppingItemSerializer,
            400: "Bad Request",
            404: "Not Found"
        }
    )
    def put(self, request, name):
        try:
            item = ShoppingItem.objects.get(name=name)
        except ShoppingItem.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

        data=request.data.copy()
        data['name'] = name
        serializer = ShoppingItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a shopping item",
        manual_parameters=[
            openapi.Parameter(
                'name',
                openapi.IN_PATH,
                description="Name of the shopping item to delete",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            204: "No Content",
            404: "Not Found"
        }
    )
    def delete(self, request, name):
        try:
            item = ShoppingItem.objects.get(name=name)
        except ShoppingItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
            return Response(status=status.HTTP_204_NO_CONTENT)

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


