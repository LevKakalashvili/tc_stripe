import stripe
import os
import decimal

from dotenv import load_dotenv
from requests import Session
from stripe_app.models import ItemNamedTuple

load_dotenv()


class StripeManager:
    def __init__(self):
        self._stripe = stripe
        self._stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

    def _create_checkout_session(self, product: ItemNamedTuple, currency: str, quantity: int) -> Session:
        session: Session = self._stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": currency,
                        "product_data": {
                            "name": product.name,
                            "description": product.description,
                        },
                        "unit_amount": product.price * 100,
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

        return session.url # type: ignore

    def get_payment_session_id(self, product: ItemNamedTuple, currency: str, quantity: int) -> str:
        session: Session = self._create_checkout_session(product, currency, quantity)

        return session.id  # type: ignore
