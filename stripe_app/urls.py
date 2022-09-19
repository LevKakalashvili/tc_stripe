from django.urls import include, path
# from django.conf.urls
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from stripe_app.views import ProductListView, ProductBuyView


API_PATH = "api"

urlpatterns = [
    path(f"{API_PATH}/items/", ProductListView.as_view()),
    path(f"{API_PATH}/buy/<str:item_uuid>", ProductBuyView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
