from django.contrib import admin

# Register your models here.
from .models import News, Comment

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_date','published_date')

admin.site.register(News, NewsAdmin)
admin.site.register(Comment)