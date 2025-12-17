from collections import defaultdict
from datetime import timedelta
from django.shortcuts import render
from .forms import StayBookingForm, ActivityBookingForm
from .models import Booking
from core.models import Room


def booking_home(request):
    stay_form = StayBookingForm(prefix="stay")
    activity_form = ActivityBookingForm(prefix="activity")

    rooms = Room.objects.all()
    total_rooms = rooms.count()

    booked_per_date = defaultdict(set)

    bookings = Booking.objects.exclude(room__isnull=True)

    for booking in bookings:
        current = booking.check_in
        while current <= booking.check_out:
            booked_per_date[current].add(booking.room_id)
            current += timedelta(days=1)

    unavailable_dates = [
        date.strftime("%Y-%m-%d")
        for date, rooms_booked in booked_per_date.items()
        if len(rooms_booked) >= total_rooms
    ]

    context = {
        "stay_form": stay_form,
        "activity_form": activity_form,
        "unavailable_dates": unavailable_dates,
    }

    return render(request, "booking/booking_home.html", context)
