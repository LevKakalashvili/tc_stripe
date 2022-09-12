from django.shortcuts import render

from rest_framework import viewsets

from stripe_app.serializers import ItemSerializer
from stripe_app.models import Item
from rest_framework.views import APIView
from rest_framework.response import Response


# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all().order_by("name")
#     serializer_class = ItemSerializer


class ItemsListView(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
