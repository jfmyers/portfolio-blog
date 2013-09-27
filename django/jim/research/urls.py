from django.conf.urls import patterns, url

from research import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
)