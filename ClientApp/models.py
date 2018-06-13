from django.db import models
from tags.models import Tag
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ShortName = models.CharField(max_length=50, blank=True, null=True, default='')
    Birthdate = models.DateField(blank=True, null=True)
    Phone = models.CharField(max_length=15, blank=True, null=True, default='')
    Email = models.EmailField(blank=True, null=True)
    Site = models.URLField(default='https://vk.com', blank=True, null=True)
    SOCIAL_STATUS = (
        ('1','Школьник'),
        ('2','Студент'),
        ('3','Работающий'),
        ('4','Безработный'),
        ('0','Неизвестно')
    )
    SEX = (
        ('1','муж'),
        ('0','жен')
    )
    Social_status = models.CharField(choices=SOCIAL_STATUS, max_length=2,default='0')
    Sex = models.CharField(choices=SEX,  max_length=2,default='1')
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        client = Client.objects.create(user=kwargs['instance'])
        client.ShortName = client.user.username
        client.save()

post_save.connect(create_profile,sender=User)


class Achievment(models.Model):
    Name = models.CharField(max_length=20, blank=False, null=False)
    Description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.Name

        