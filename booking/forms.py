from django import forms
from .models import Booking
from core.models import Service


class StayBookingForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(category='accommodation'),
        empty_label="Select accommodation"
    )

    multi_dates = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control datepicker',
            'placeholder': 'Select dates'
        }),
        required=True,
        label="Select your stay dates"
    )

    class Meta:
        model = Booking
        fields = [
            'full_name',
            'email',
            'phone_number',
            'number_of_guests',
            'service',
            'multi_dates',
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
        widgets = {
            'check_in': forms.TextInput(attrs={
                'class': 'form-control datepicker',
                'placeholder': 'YYYY-MM-DD'
            }),
            'check_out': forms.TextInput(attrs={
                'class': 'form-control datepicker',
                'placeholder': 'YYYY-MM-DD'
            }),
        }
