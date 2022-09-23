from typing import NamedTuple

import stripe
import os
import decimal

import uuid as uuid
from dotenv import load_dotenv
from requests import Session

load_dotenv()


class ItemNamedTuple(NamedTuple):
    uuid: uuid.UUID
    name: str
    name: str
    description: str
    price: decimal.Decimal


class StripeManager:
    def __init__(self):
        self._stripe = stripe
        self._stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

    def _create_checkout_session(self, product: ItemNamedTuple, currency: str, quantity: decimal.Decimal) -> Session:
        session: Session = self._stripe.checkout.Session.create(
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

    # def get_payment_url(self, name: str, price: decimal, currency: str, quantity: int) -> str:
    #     session: Session = self._create_checkout_session()

        return session.url  # type: ignore

    def get_payment_session_id(self, product: ItemNamedTuple, currency: str, quantity: decimal.Decimal) -> str:
        session: Session = self._create_checkout_session(product, currency, quantity)

        return session.id  # type: ignore
