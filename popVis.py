from ShopApp.models import Visit
from ClientApp.models import Client

from django.contrib.auth.models import User
import random
from random import randrange
from datetime import datetime, date, time, timedelta


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2018, 1, 1)
end_date = date(2018, 12, 30)


Visit.objects.filter(Note__icontains='Autovisit').delete()

for single_date in daterange(start_date, end_date):
	print (single_date)
	a = random.randint(10,76) #visits per day
	for x in range(1,a):
		try:
			cl = Client.objects.get(id=random.randint(2,125))
		except Client.DoesNotExist:
			cl = Client.objects.get(id=20)
		c = Visit(
			id_client = cl,
			id_manager = User.objects.get(id=2),
			Date = single_date,
			Note = 'Autovisit '+str(x)
		)
		c.save()
		pass