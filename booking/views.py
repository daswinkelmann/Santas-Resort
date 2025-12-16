from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def booking_home(request):
    return HttpResponse("Booking app is working")
