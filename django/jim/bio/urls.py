from django.conf.urls import patterns, url

from bio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)