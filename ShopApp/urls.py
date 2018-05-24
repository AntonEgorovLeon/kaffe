from django.conf.urls import url

from . import views

app_name = 'ShopApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^charts/', views.charts, name='charts'),
    url(r'^charts_get/', views.charts_get, name='charts_get'),
    url(r'^clientAutoComplete/', views.client_auto, name='clientAuto'),
]