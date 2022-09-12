from django.urls import include, path
from rest_framework import routers
from stripe_app.views import ItemViewSet

router = routers.DefaultRouter()
router.register("items", ItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]