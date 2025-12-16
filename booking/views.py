from django.shortcuts import render
from .forms import StayBookingForm, ActivityBookingForm


# Create your views here.
def booking_home(request):
    stay_form = StayBookingForm(prefix='stay')
    activity_form = ActivityBookingForm(prefix='activity')

    if request.method == 'POST':
        if 'stay-submit' in request.POST:
            stay_form = StayBookingForm(
                request.POST, prefix='stay'
                )
            if stay_form.is_valid():
                stay_form.save()
                # return Redirect

        elif 'activity-submit' in request.POST:
            activity_form = ActivityBookingForm(
                request.POST, prefix='activity'
                )
            if activity_form.is_valid():
                activity_form.save()
                # return Redirect

    context = {
        'stay_form': stay_form,
        'activity_form': activity_form,
    }
    return render(request, 'booking/booking_home.html', context)
