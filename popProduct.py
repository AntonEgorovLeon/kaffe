from ShopApp.models import Good
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





#for Python2 replace (for x in xrange(8,200):)
# m = 'Событие'
Good.objects.filter(Description__icontains='AutoDescription').delete()
for x in range(1,100):
	cat=str(int(random.triangular(1,3,2)))
	c = Good(
		Name='AutoProduct'+str(x), 
		Description='AutoDescription',
		Category = cat,
		Price = x*8/10,
		FreeAmount = int(random.triangular(1,8,4)),
		HoldAmountBuy = int(random.triangular(1,4,2)),
		HoldAmountSale =int(random.triangular(1,4,4))
	)
	c.save()
