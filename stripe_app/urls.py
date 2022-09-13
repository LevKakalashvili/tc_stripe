from django.urls import include, path
# from django.conf.urls
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from stripe_app.views import ItemsListView, ItemBuyView


API_PATH = "api"

urlpatterns = [
    path(f"{API_PATH}/items/", ItemsListView.as_view()),
    path(f"{API_PATH}/buy/<str:item_uuid>", ItemBuyView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
