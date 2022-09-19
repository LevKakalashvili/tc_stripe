import stripe
import os

from dotenv import load_dotenv
from requests import Session

load_dotenv()


class StripeManager:
    def __init__(self):
        self._stripe = stripe
        self._stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

    def _create_checkout_session(self) -> Session:
        session: Session = self._stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "T-shirt",
                        },
                        "unit_amount": 2000,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )

        return session

    def get_payment_url(self) -> str:
        session: Session = self._create_checkout_session()

        return session.url

