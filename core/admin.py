from django.contrib import admin
from .models import Service, Amenity, Room

admin.site.register(Amenity)
admin.site.register(Room)
admin.site.register(Service)


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'category',
                    'price',
                    'status',
                    'is_active')
    list_filter = ('category', 'status', 'is_active')
    search_fields = ('name', 'description')


class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'icon',
                    'is_available'
                    )
    list_filter = ('is_available',)
    search_fields = ('name', 'description')


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'status',
        'is_available'
        )
    list_filter = ('status', 'is_available')
    search_fields = ('number', 'description')
    filter_horizontal = ('amenities',)
