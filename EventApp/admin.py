from django.contrib import admin

# Register your models here.
from .models import EventTemplate, Event

admin.site.register(Event)
admin.site.register(EventTemplate)