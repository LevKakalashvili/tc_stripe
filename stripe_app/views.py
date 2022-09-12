from django.shortcuts import render

from rest_framework import viewsets

from stripe_app.serializers import ItemSerializer
from stripe_app.models import Item

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("name")
    serializer_class = ItemSerializer
