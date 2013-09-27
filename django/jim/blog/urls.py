from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    # ex: /posts
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<post_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<post_id>\d+)/comment/$', views.comment, name='comment'),
    # ex: /posts/5/
    #url(r'^(?P<post_id>\d+)/$', views.detail, name='detail')
)