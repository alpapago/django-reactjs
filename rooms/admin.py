from django.contrib import admin
from rooms.models import Amenity, Rooms

@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )
    list_filter = (
        'name',
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass