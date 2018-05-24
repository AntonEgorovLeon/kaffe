from django.conf.urls import url

from . import views


app_name = 'registration'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^reg/$', views.registration, name='reg'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^profile_change/$', views.profile_change, name='profile_change'),
]