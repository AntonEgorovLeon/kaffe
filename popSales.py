from ShopApp.models import Sale ,Good
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

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)
d1 = datetime(1962, 7, 14)
d2 = datetime(2005, 7, 14)

SS = ['0', '1', '2', '3']
SX = ['0', '1']


# class Sale (models.Model):
#     id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     id_product  = models.ForeignKey(Product, on_delete=models.CASCADE)
#     id_manager = models.ForeignKey('auth.User', default='1')
#     Date = models.DateField(blank=True, null=True)
#     Note = models.CharField(max_length=50, blank=True, null=True)
#     STATUS = (
#         ('1','Завершен'),
#         ('2','В процессе'),
#         ('3','Отменен')
#     )
#     Status = models.CharField(choices=STATUS, max_length=2,default='1')
#     def __str__(self):
#         return str(self.pk)


# Product.objects.filter(login__icontains='AutoUser').delete()
#for Python2 replace (for x in xrange(8,200):)
# m = 'Событие'
# for x in range(1,100):


Sale.objects.filter(Note__icontains='AutoSale').delete()
start_date = date(2018, 1, 1)
end_date = date(2018, 12, 3)
for single_date in daterange(start_date, end_date):
	print (single_date)
	a = random.randint(10,51)
	for x in range(1,a):
		try:
			cl = Client.objects.get(id=random.randint(2,125))
		except Client.DoesNotExist:
			cl = Client.objects.get(id=20)
		rint=random.randint(2,100)
		c = Sale(
			id_client = cl,
		    id_product  = Good.objects.get(pk=rint), #need to increase number of event class product here
		    id_manager = User.objects.get(id=2),
		    Date = single_date,
		    Status = '1',
		    Note = 'AutoSale'
		)
		c.save()