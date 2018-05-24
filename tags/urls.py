from django.conf.urls import url
from tags.views import TagMixin

app_name = 'tags'
urlpatterns = [
    url(r'^ajax_add_tag/$', TagMixin.ajax_add_tag, name="ajax-add-tag")
]