from django.conf import settings

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from stripe_app.models import Item
from stripe_app.manager import stripe_manager
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

        data = {session_id}
        return Response(data=data)


class ProductDetailView(DetailView):
    model = Item

    def get_object(self):
        return get_object_or_404(Item, pk=self.kwargs["item_uuid"])

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["STRIPE_PUBLISHABLE_API_KEY"] = settings.STRIPE_PUBLISHABLE_API_KEY
        context["api_request_url"] = f"{'http://'}" \
                                     f"{self.request.headers.get('Host')}" \
                                     f"{self.request.path.replace('item', 'buy')}"
        return context
