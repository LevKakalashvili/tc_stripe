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
            return Item.objects.get(pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        item = self.get_object(pk).get_tuple()
        session_id = stripe_manager.get_payment_session_id(
            name=item.name,
            price=item.price,
            description=item.description,
            currency="rub",
            quantity="1",
            )

        data = {
            "success": True,
            "stripe_session_id": session_id
        }
        return Response(data=data)

    # def get():
    # def get(self, request, format=None):
    #     a = 1
    #
    #     # product = Item(uuid=uuid.uuid4(), name="Товар 1", description="Описание", price=99.00)
    #     # product.save()
    #     # product = Item.objects.get(uuid__exact=uuid.UUID(item_uuid))
    #     # redirect_url = stripe_manager.get_payment_url()
    #     # session_id = stripe_manager.get_payment_session_id()
    #     # # serializer = ItemSerializer(product, many=True)
    #     # data = {"status": "Ok", "stripe_session_id": session_id}
    #     # return Response(data=data)
    #     # # return redirect(redirect_url)
    #     # a = 1
    #     return Response()

#
# class ProductListView(APIView):
#     def get(self, request, format=None):
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)
