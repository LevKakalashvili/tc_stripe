from dataclasses import fields

from rest_framework import serializers

from stripe_app.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("uuid", "name", "description", "price")