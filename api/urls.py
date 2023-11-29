from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlatformListViewSet,PlatformDetailViewSet

router = DefaultRouter()
router.register(r"platforms", PlatformListViewSet)
# router.register(r"platform/<int:pk>", PlatformDetailViewSet)

urlpatterns = [
    path("v1/", include(router.urls))
]