from django.contrib import admin

from .models import Sale, Good, Visit
# Register your models here.

admin.site.register(Sale)
admin.site.register(Good)
admin.site.register(Visit)