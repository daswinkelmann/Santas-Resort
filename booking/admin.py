from django.contrib import admin
from .models import Booking

admin.site.register(Booking)


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'service', 'check_in', 'check_out',
        'number_of_guests', 'total_price', 'created_at'
        )
    list_filter = ('check_in', 'check_out', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number', 'special_requests')
