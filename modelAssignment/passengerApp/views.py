from django.shortcuts import render
from passengerApp.models import Passenger
# Create your views here.


def passengerData(request):
    passengers = Passenger.objects.all()
    passengerDict = {'passengers' : passengers}
    return render(request, 'passengerApp/passengers.html', passengerDict)
