from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import PlatformSerializer, GameSerializer, DeviceSerializer, SouvenirSerializer
from .models import Platform, Game, Device, Souvenir


class PlatformListViewSet(viewsets.ViewSet):
    """

    """
    queryset = Platform.objects.all()

    def list(self, request):
        serializer = PlatformSerializer(self.queryset, many=True, context={'request': request})
        return Response(serializer.data)


class PlatformDetailViewSet(viewsets.ViewSet):
    """

    """
    queryset = Platform.objects.all()

    def retrieve(self, request, pk=None):
        platform = self.queryset.filter_by(id=pk)
        serializer = PlatformSerializer(platform, many=False, context={"request": request})
        return Response(serializer.data)


# class PlatformCreateViewSet(viewsets.ViewSet):
#     """
#
#     """
#
#     def create(self, request):
#         payload = request.data
#         platform = Platform.objects.create(
#             title=payload["title"],
#             slug=payload["slug"],
#             information=payload["information"]
#         )
#         serializer = PlatformSerializer(platform, many=False, context={'request': request})
#         return Response(serializer.data)
#
#
# class PlatformUpdateViewSet(viewsets.ViewSet):
#     """
#
#     """
#
#     def update(self, request):
#         platform = Platform.objects.update(request.data)
#         serializer = PlatformSerializer(platform)
#         return Response(serializer.data)


# class GameList(viewsets.ViewSet):
#     """
#
#     """
#
#     def list(self, request):
#         serializer = GameSerializer(Game.objects.all().prefetch_related(), many=True, context={'request': request})
#         return Response(serializer.data)
#
#
# class DeviceList(viewsets.ViewSet):
#     """
#
#     """
#
#     def list(self, request):
#         serializer = DeviceSerializer(Device.objects.all(), many=True, context={'request': request})
#         return Response(serializer.data)
#
#
# class SouvenirList(viewsets.ViewSet):
#     """
#
#     """
#
#     def list(self, request):
#         serializer = SouvenirSerializer(Souvenir.objects.all(), many=True, context={'request': request})
#         return Response(serializer.data)
