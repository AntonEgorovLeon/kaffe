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

# foo = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(foo))
# print('a')

# class Client(models.Model):
#     id_role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     login = models.CharField(max_length=20, blank=True, null=True)
#     full_name = models.CharField(max_length=30, blank=True, null=True)
#     pwd = models.CharField(max_length=10, blank=True, null=True)
#     begindate = models.DateField(blank=True, null=True)
#     birthdate = models.DateField(blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     site = models.CharField(max_length=50, blank=True, null=True)
#     SOCIAL_STATUS = (
#         (1,'school'),
#         (2,'student'),
#         (3,'worker'),
#         (0,'dependent')
#     )
#     SEX = (
#         (1,'male'),
#         (0,'female')
#     )
#     social_status = models.CharField(choices=SOCIAL_STATUS, max_length=2,default=0)
#     sex = models.CharField(choices=SEX,  max_length=2,default=1)

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