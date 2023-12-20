from django.contrib import admin
from rooms.models import Amenity, Room


@admin.register(Room)
class RoomsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )
    list_filter = ("name",)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass
