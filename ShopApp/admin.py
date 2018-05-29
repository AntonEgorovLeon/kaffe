from django.contrib import admin

from .models import Sale, Good, Visit
# Register your models here.

class SaleAdmin(admin.ModelAdmin):
    # fields = ['pk','id_client', 'id_product','Date','Status']
    list_display = ('pk','id_client', 'id_manager', 'id_product','Date','Status')

class VisitAdmin(admin.ModelAdmin):
    list_display = ('pk','id_client', 'id_manager','Date','Note')

admin.site.register(Sale, SaleAdmin)
admin.site.register(Good)
admin.site.register(Visit, VisitAdmin)