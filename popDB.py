from ClientApp.models import Client
from django.contrib.auth.models import User 

import random
from random import randrange
from datetime import datetime, date, time, timedelta

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime(1962, 7, 14)
d2 = datetime(2005, 7, 14)

SS = ['0', '1', '2', '3']
SX = ['0', '1']

Client.objects.filter(ShortName__icontains='AutoUser').delete()
User.objects.filter(username__icontains='AutoCreated').delete()

# x=35
for x in range(50,125):
	u = User.objects.create(pk=x,
							username='AutoCreated'+str(x+2*x)+str(x)+str(2*x),
							email=str(x+3)+str(x)+str(2*x)+'@dfsefg.com',
							password=str(x+7)+str(x*2)+str(2*x)+'few'+str(x+3*x))
	print('created')
	c = Client(
		user=u,
		ShortName='AutoUser'+str(x), 
		Birthdate=random_date(d1, d2), 
		Social_status=random.choice(SS), 
		Sex=random.choice(SX)
	)
	c.save()
	pass