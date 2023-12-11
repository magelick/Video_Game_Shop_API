from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PlatformSerializer, GameSerializer, DeviceSerializer, SouvenirSerializer
from .models import Platform, Game, Device, Souvenir


class PlatformList(APIView):
    """
    Ручка для отображения списка всех платформ и создание конкретной платформы
    """

    def get(self, request):
        serializer = PlatformSerializer(Platform.objects.all(), many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        platform = Platform.objects.create(
            title=request.data["title"],
            information=request.data["information"]
        )
        platform.slug = slugify(request.data["title"])
        serializer = PlatformSerializer(platform, many=False, context={"request": request})
        return Response(serializer.data)


class PlatformDetail(APIView):
    """
    Ручка для получения конкретной платформы, её изменения или удаления
    """

    def get(self, request, pk=None):
        platform = Platform.objects.filter(id=pk)
        serializer = PlatformSerializer(platform, many=True, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk=None):
        platform = get_object_or_404(Platform, id=pk)
        serializers = PlatformSerializer(instance=platform, data=request.data, context={"request": request})
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

    def delete(self, request, pk=None):
        platform = get_object_or_404(Platform, id=pk)
        platform.delete()
        return Response({"msg": "Done"})


class GameList(APIView):
    """
    Ручка для отображения списка всех игр и создание конкретной игры
    """

    def get(self, request):
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        game = Game.objects.create(
            title=request.data["title"],
            slug=request.data["slug"],
            price=request.data["price"],
        )
        platforms = Platform.objects.filter(id__in=request.data["platform"])
        game.platform.set(platforms)
        serializer = GameSerializer(game, context={"request": request})
        return Response(serializer.data)


class GameDetail(APIView):
    """
    Ручка для получения конкретной игры, её изменения или удаления
    """

    def get(self, request, pk=None):
        game = Game.objects.filter(id=pk)
        serializer = GameSerializer(game, many=True, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk=None):
        game = Game.objects.filter(Game, id=pk)
        serializer = GameSerializer(game, data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=None):
        game = get_object_or_404(Game, id=pk)
        game.delete()
        return Response({"msg": "Done"})


class GamesOfPlatform(APIView):
    """
    Ручка для получения всех игр конкретной платформы
    """

    def get(self, request, pk=None):
        platform = Platform.objects.get(id=pk)
        games = platform.games.all()
        serializer = GameSerializer(games, many=True, context={"request": request})
        return Response(serializer.data)


class PlatformsOfGame(APIView):
    """
    Ручка для получения всех платформ конкретной игры
    """

    def get(self, request, pk=None):
        game = Game.objects.get(id=pk)
        platforms = game.platform.all()
        serializer = PlatformSerializer(platforms, many=True, context={"request": request})
        return Response(serializer.data)


class DeviceList(APIView):
    """
    Ручка для отображения списка всех девайсов и создание конкретного девайса
    """

    def get(self, request):
        device = Device.objects.all()
        serializer = DeviceSerializer(device, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        platform = Platform.objects.get(id=request.data["platform"])
        device = Device.objects.create(
            title=request.data["title"],
            slug=request.data["slug"],
            information=request.data["information"],
            price=request.data["price"],
            platform=platform
        )
        serializer = DeviceSerializer(device, context={"request": request})
        return Response(serializer.data)


class DeviceDetail(APIView):
    """
    Ручка для получения конкретного девайса, его изменения или удаления
    """

    def get(self, request, pk=None):
        device = Device.objects.filter(id=pk)
        serializer = DeviceSerializer(device, many=True, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk=None):
        device = Device.objects.filter(id=pk)
        serializer = DeviceSerializer(device, data=request.data, many=True, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=None):
        device = get_object_or_404(Device, id=pk)
        device.delete()
        return Response({"msg": "Done"})


class DevicesOfPlatform(APIView):
    """
    Ручка для получения всех девайсов конкретной платформы
    """

    def get(self, request, pk=None):
        platform = Platform.objects.get(id=pk)
        devices = platform.devices.all()
        serializer = DeviceSerializer(devices, many=True, context={"request": request})
        return Response(serializer.data)


class SouvenirList(APIView):
    """
    Ручка для отображения списка всех сувениров и создание конкретног сувенира
    """

    def get(self, request):
        souvenirs = Souvenir.objects.all()
        serializer = SouvenirSerializer(souvenirs, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        game = Game.objects.get(id=request.data["game"])
        souvenir = Souvenir.objects.create(
            title=request.data["title"],
            slug=request.data["slug"],
            information=request.data["information"],
            price=request.data["price"],
            game=game
        )
        serializer = SouvenirSerializer(souvenir, context={"request": request})
        return Response(serializer.data)


class SouvenirDetail(APIView):
    """
    Ручка для получения конкретного сувенира, его изменения или удаления
    """

    def get(self, request, pk=None):
        souvenirs = Souvenir.objects.filter(id=pk)
        serializer = SouvenirSerializer(souvenirs, many=True, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk=None):
        souvenirs = Souvenir.objects.get(id=pk)
        serializer = SouvenirSerializer(souvenirs, data=request.data, many=True, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=None):
        souvenirs = get_object_or_404(Souvenir, id=pk)
        souvenirs.delete()
        return Response({"msg": "Done"})


class SouvenirsOfGame(APIView):
    """
    Ручка для получения всех сувениров конкретной игры
    """
    def get(self, request, pk=None):
        game = Game.objects.get(id=pk)
        platforms = game.souvenirs.all()
        serializer = SouvenirSerializer(platforms, many=True, context={"request": request})
        return Response(serializer.data)

