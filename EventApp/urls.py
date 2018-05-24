from django.conf.urls import url

from . import views

app_name = 'EventApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clientList/', views.IndexView.as_view(), name='indexView'),
]