import uuid

from django.shortcuts import redirect

from stripe_app.serializers import ItemSerializer
from stripe_app.models import Item
from stripe_app import stripe_manager
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductBuyView(APIView):
    def get(self, request, item_uuid: str, format=None):
        product = Item(uuid=uuid.uuid4(), name="Товар 1", description="Описание", price=99.00)
        # product.save()
        # product = Item.objects.all().filter(uuid__exact=uuid.UUID(item_uuid))[0]
        redirect_url = stripe_manager.get_payment_url()
        # serializer = ItemSerializer(product, many=True)
        # return Response(serializer.data)
        return redirect(redirect_url)


class ProductListView(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
