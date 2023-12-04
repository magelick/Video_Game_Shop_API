from django.urls import path
from .views import (
    PlatformList,
    PlatformDetail,
    GameList,
    GameDetail,
    GamesOfPlatform,
    PlatformsOfGame,
    DeviceList,
    DeviceDetail,
    DevicesOfPlatform,
    SouvenirList,
    SouvenirDetail,
    SouvenirsOfGame
)

urlpatterns = [
    path("v1/platforms/", PlatformList.as_view()),
    path("v1/platforms/<int:pk>/", PlatformDetail.as_view()),
    path("v1/platforms/<int:pk>/games/", GamesOfPlatform.as_view()),
    path("v1/platforms/<int:pk>/devices/", DevicesOfPlatform.as_view()),
    path("v1/games/", GameList.as_view()),
    path("v1/games/<int:pk>/", GameDetail.as_view()),
    path("v1/games/<int:pk>/platforms/", PlatformsOfGame.as_view()),
    path("v1/games/<int:pk>/souvenirs/", SouvenirsOfGame.as_view()),
    path("v1/devices/", DeviceList.as_view()),
    path("v1/devices/<int:pk>/", DeviceDetail.as_view()),
    path("v1/souvenirs/", SouvenirList.as_view()),
    path("v1/souvenirs/<int:pk>/", SouvenirDetail.as_view()),
]