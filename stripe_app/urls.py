from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from stripe_app.views import ItemsListView
#
# router = routers.DefaultRouter()
# router.register("items", ItemViewSet)

urlpatterns = [
    path('api/items/', ItemsListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
