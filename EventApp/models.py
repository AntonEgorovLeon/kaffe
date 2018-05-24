from django.db import models
from tags.models import Tag

	
class EventTemplate(models.Model):
    Name = models.CharField(max_length=50, blank=False, null=False)
    Descrition = models.TextField(max_length=50, blank=True, null=True)
    Category = models.CharField(max_length=50, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.Name

class Event(models.Model):
    id_event = models.ForeignKey(EventTemplate, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=9, decimal_places=2)
    Date = models.DateField(blank=False, null=False)
    def __str__(self):
        return self.Name