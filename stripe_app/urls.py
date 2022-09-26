from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from stripe_app.views import ProductDetailView, ProductApiBuyView


API_PATH = "api/v1"

urlpatterns = [
    path(f"{API_PATH}/item/<str:item_uuid>", ProductDetailView.as_view()),
    path(f"{API_PATH}/buy/<str:item_uuid>", ProductApiBuyView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
