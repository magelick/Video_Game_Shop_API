from rest_framework import serializers

from .models import Platform, Game, Device, Souvenir


class PlatformSerializer(serializers.ModelSerializer):
    """
    Серилизатор модели Платформ со всеми полями
    """

    class Meta:
        model = Platform
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    """
    Серилизатор модели Игр со всеми полями
    """
    platform = PlatformSerializer(many=True)

    class Meta:
        model = Game
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    """
    Серилизатор модели Игр со всеми полями
    """
    platform = PlatformSerializer()

    class Meta:
        model = Device
        fields = "__all__"


class SouvenirSerializer(serializers.ModelSerializer):
    """
    Серилизатор модели Сувениров со всеми полями
    """
    game = GameSerializer()

    class Meta:
        model = Souvenir
        fields = "__all__"
