from django.conf.urls import url

from . import views

app_name = 'NewsApp'
urlpatterns = [
    url('^$', views.NewsList.as_view()),
    url(r'^(?P<pk>\d+)/$', views.NewsDetail.as_view())
]