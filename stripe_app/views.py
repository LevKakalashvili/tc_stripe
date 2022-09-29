from urllib.parse import urljoin

from django.conf import settings

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from stripe_app.models import Item
from stripe_app import stripe_manager
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductApiBuyView(APIView):

    def get_object(self, item_uuid) -> Item:
        return get_object_or_404(Item, pk=item_uuid)

    def get(self, request, item_uuid, format=None) -> Response:

        item = self.get_object(item_uuid)
        item = item.get_tuple()
        session_id = stripe_manager.get_payment_session_id(
            product=item,
            currency="rub",
            quantity="1",
            )

        # data = {"success": True, "stripe_session_id": session_id}
        data = {session_id}
        return Response(data=data)


class ProductDetailView(DetailView):
    model = Item

    def get_object(self):
        return get_object_or_404(Item, pk=self.kwargs["item_uuid"])

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["STRIPE_PUBLISHABLE_API_KEY"] = settings.STRIPE_PUBLISHABLE_API_KEY
        context["api_request_url"] = "".join(["http://", self.request.headers.get("Host"), self.request.path.replace("item", "buy")])
        return context


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
