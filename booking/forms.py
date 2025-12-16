from django import forms
from .models import Booking
from core.models import Service


class StayBookingForm(forms.ModelForm):

    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(category='accommodation'),
        empty_label="Select accommodation"
    )

    class Meta:
        model = Booking
        fields = [
            'full_name',
            'email',
            'phone_number',
            'number_of_guests',
            'service',
            'check_in',
            'check_out',
            'special_requests',
            'total_price'
            ]


class ActivityBookingForm(forms.ModelForm):

    service = forms.ModelChoiceField(
        queryset=Service.objects.exclude(category='accommodation'),
        empty_label="Select activity"
    )

    class Meta:
        model = Booking
        fields = [
            'full_name',
            'email',
            'phone_number',
            'number_of_guests',
            'service',
            'check_in',
            'special_requests',
            'total_price'
            ]
