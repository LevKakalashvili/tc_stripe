import decimal
from dataclasses import dataclass
from typing import NamedTuple

import stripe
import uuid as uuid

from django.conf import settings
from requests import Session


class ItemNamedTuple(NamedTuple):
    uuid: uuid.UUID
    name: str
    name: str
    description: str
    price: decimal.Decimal


@dataclass
class StripeManager:
    def __init__(self):
        self._stripe = stripe
        self._stripe.api_key = settings.STRIPE_SECRET_KEY

    def _create_checkout_session(
        self, product: ItemNamedTuple, currency: str, quantity: int
    ) -> Session:
        session = self._stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": currency,
                        "product_data": {
                            "name": product.name,
                            "description": product.description,
                        },
                        "unit_amount": int(product.price * 100),
                    },
                    "quantity": quantity,
                }
            ],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )

        return session

    def get_payment_session_id(
        self, product: ItemNamedTuple, currency: str, quantity: int
    ) -> str:
        session = self._create_checkout_session(product, currency, quantity)

        return session.id


stripe_manager = StripeManager()