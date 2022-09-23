from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from stripe_app.views import ProductBuyView


API_PATH = "api"

urlpatterns = [
    # path(f"{API_PATH}/items/", ProductListView.as_view()),
    path(f"{API_PATH}/buy/<pk>", ProductBuyView.as_view()),
    # path(f"{API_PATH}/buy/(?P<id>[0-9a-f-]+)", ProductBuyView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
