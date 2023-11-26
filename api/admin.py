from django.contrib import admin
from .models import Platform, Game, Device, Souvenir


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "information")
    search_fields = ("title",)
    prepopulated_fields = {
        "slug": ("title",)
    }


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "price",)
    list_filter = ("price", "platform")
    list_editable = ("price",)
    search_fields = ("title",)
    prepopulated_fields = {
        "slug": ("title", "price", "platform")
    }


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "price", "information", "platform")
    list_filter = ("price",)
    list_editable = ("price",)
    search_fields = ("title",)
    prepopulated_fields = {
        "slug": ("title", "price", "platform")
    }


@admin.register(Souvenir)
class SouvenirAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "price", "information", "game")
    list_filter = ("price",)
    list_editable = ("price",)
    search_fields = ("title",)
    prepopulated_fields = {
        "slug": ("title", "price", "game")
    }
