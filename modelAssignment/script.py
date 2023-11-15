from passengerApp.models import Passenger
from django.db.models import Max

qs=Passenger.objects.all()
print(qs)
qs=qs.all().values_list('firstName', 'lastName')
print(qs)
qs=Passenger.objects.all().order_by('rewardPoints')
print(qs)
qs=qs.all().aggregate(Max('rewardPoints'))
print(qs)