import uuid

from django.shortcuts import render

from rest_framework import viewsets

from stripe_app.serializers import ItemSerializer
from stripe_app.models import Item
from rest_framework.views import APIView
from rest_framework.response import Response

class ItemBuyView(APIView):
    def get(self, request, item_uuid: str, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class ItemsListView(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
