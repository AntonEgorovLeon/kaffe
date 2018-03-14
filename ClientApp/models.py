from django.db import models

class Client(models.Model):
    ShortName = models.CharField(max_length=20, blank=True, null=True)
    Last_name = models.CharField(max_length=30, blank=True, null=True)
    First_name = models.CharField(max_length=30, blank=True, null=True)
    Second_name = models.CharField(max_length=30, blank=True, null=True)
    Birthdate = models.DateField(blank=True, null=True)
    Phone = models.CharField(max_length=15, blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)
    Site = models.CharField(max_length=50, blank=True, null=True)
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
    def __str__(self):
        return self.ShortName


class Achievment(models.Model):
    """docstring for Achievment"""
    Name = models.CharField(max_length=20, blank=False, null=False)
    Description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.Name

        