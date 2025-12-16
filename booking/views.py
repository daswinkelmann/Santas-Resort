from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def book_stay(request):
    return render(request, 'booking/stay.html')


def book_activities(request):
    return render(request, 'booking/activities.html')
