from django.urls import path, include
from rest_framework.routers import SimpleRouter

router = SimpleRouter()


urlpatterns = [
    path("v1/", include(router.urls))
]