from rest_framework import serializers

from .models import Platform, Game, Device, Souvenir


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    """
    Серилизатор модели Платформ со всеми полями
    """

    class Meta:
        model = Platform
        fields = ("id", "title", "slug", "information")


class GameSerializer(serializers.HyperlinkedModelSerializer):
    """
    Серилизатор модели Игр со всеми полями
    """
    platform = PlatformSerializer(many=True)

    class Meta:
        model = Game
        fields = ("id", "title", "slug", "price", "platform")


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    """
    Серилизатор модели Игр со всеми полями
    """
    platform = PlatformSerializer()

    class Meta:
        model = Device
        fields = ("id", "title", "slug", "price", "platform")


class SouvenirSerializer(serializers.ModelSerializer):
    """
    Серилизатор модели Сувениров со всеми полями
    """
    game = GameSerializer()

    class Meta:
        model = Souvenir
        fields = ("title", "slug", "information", "price", "game")
