import uuid

from django.http import Http404
from django.shortcuts import redirect
from rest_framework.generics import RetrieveAPIView

from stripe_app.serializers import ItemSerializer
from stripe_app.models import Item
from stripe_app import stripe_manager
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductBuyView(APIView):

    def get_object(self, pk) -> Item:
        try:
            return Item.objects.get(uuid=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        try:
            uuid.UUID(pk)
        except ValueError:
            raise Http404

        item = self.get_object(pk)
        item = item.get_tuple()
        session_id = stripe_manager.get_payment_session_id(
            product=item,
            currency="rub",
            quantity=1,
            )

        data = {
            "success": True,
            "stripe_session_id": session_id
        }
        return Response(data=data)


# class ProductListView(APIView):
#     def get(self, request, format=None):
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)
