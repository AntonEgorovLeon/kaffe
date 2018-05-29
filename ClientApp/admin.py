from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Client, Achievment

# Define an inline admin descriptor for Client model
# which acts a bit like a singleton
class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'Clients'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline, )

class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk','ShortName', 'Birthdate','Phone', 'Site')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Client, ClientAdmin)
admin.site.register(Achievment)