from django.db import models
from ClientApp.models import Client
from tags.models import Tag

class Good(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    Notes = models.TextField(blank=True, null=True)
    Price = models.DecimalField(max_digits=9, decimal_places=2)
    CATEGORY = (
        ('1','Настольные игры'),
        ('2','Коллекционные карточные игры'),
        ('3','Варгейм')
    )
    Category = models.CharField(choices=CATEGORY, max_length=2,default='1')
    FreeAmount = models.IntegerField(blank=False, null=False, default = 0)
    HoldAmountBuy = models.IntegerField(blank=False, null=False, default = 0)
    HoldAmountSale = models.IntegerField(blank=False, null=False, default = 0)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.Name

class Sale (models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_product  = models.ForeignKey(Good, on_delete=models.CASCADE)
    id_manager = models.ForeignKey('auth.User', default='1')
    Date = models.DateField(blank=False, null=False)
    DateFin = models.DateField(blank=True, null=True)
    Note = models.CharField(max_length=50, blank=True, null=True)
    STATUS = (
        ('1','Завершен'),
        ('2','В процессе'),
        ('3','Отменен')
    )
    Status = models.CharField(choices=STATUS, max_length=2,default='1')
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return str(self.pk)

class Visit (models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_manager = models.ForeignKey('auth.User', default='1')
    Date = models.DateField(blank=False, null=False)
    Note = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return str(self.pk)