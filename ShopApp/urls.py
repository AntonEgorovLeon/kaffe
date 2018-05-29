from django.conf.urls import url

from . import views

app_name = 'ShopApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^charts/', views.charts, name='charts'),
    url(r'^visits/', views.visit_add, name='visits'),
    url(r'^charts_get/', views.charts_get, name='charts_get'),
    url(r'^charts_get1/', views.charts_get1, name='charts_get1'),
    url(r'^clientAutoComplete/', views.client_auto, name='clientAuto'),
]